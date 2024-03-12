import os

import gymnasium as gym
from ray import tune
from ray.air.integrations.wandb import WandbLoggerCallback
from ray.rllib.algorithms.callbacks import DefaultCallbacks

from config import parse_configs, seed_everything

import tensorflow as tf

tf.keras.backend.set_floatx("float32")


class CustomCallback(DefaultCallbacks):
    def on_episode_end(self, worker, base_env, policies, episode, **kwargs):
        info = episode.last_info_for()
        if info is not None and "is_success" in info:
            episode.custom_metrics["success_rate"] = info["is_success"]


if __name__ == "__main__":
    configs = parse_configs("ray")
    seed_everything(configs["seed"])

    def create_env(config):
        import sliding_puzzles

        return gym.make("SlidingPuzzle-v0", **config)

    tune.registry.register_env("SlidingPuzzle", create_env)
    configs["ray"]["config"]["env"] = "SlidingPuzzle"
    configs["ray"]["config"]["env_config"] = configs["env"]
    configs["ray"]["config"]["callbacks"] = CustomCallback
    configs["ray"]["config"]["seed"] = configs["seed"]

    # training
    analysis = tune.run(
        configs["ray"]["algorithm"],
        name=configs["run_id"],
        config=configs["ray"]["config"],
        stop={
            "timesteps_total": configs["total_timesteps"],  # 15M
            # "time_total_s": 14400, # 4h
            configs["ray"]["analysis_metric"]: configs["env"]["win_reward"],
        },
        checkpoint_config={
            "checkpoint_frequency": 100,
            "checkpoint_at_end": True
        },
        local_dir=os.path.abspath(configs["logdir"]),
        restore=(
            os.path.abspath(configs["checkpoint"])
            if "checkpoint" in configs and configs["checkpoint"]
            else None
        ),
        callbacks=(
            [
                WandbLoggerCallback(
                    project=configs["wandb_project"],
                    log_config=True,
                    group=configs["experiment_name"],
                    name=configs["run_id"],
                )
            ]
            if not configs["disable_wandb"]
            else None
        ),
    )

    # Gets best trial based on max accuracy across all training iterations.
    best_trial = analysis.get_best_trial(configs["ray"]["analysis_metric"], mode="max")
    print(best_trial)
    # Gets best checkpoint for trial based on accuracy.
    best_checkpoint = analysis.get_best_checkpoint(
        trial=best_trial, metric=configs["ray"]["analysis_metric"], mode="max"
    )
    print(best_checkpoint)
    print("Done training")
