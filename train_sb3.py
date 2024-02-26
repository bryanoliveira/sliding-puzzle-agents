import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common import callbacks
from stable_baselines3.common.env_util import make_vec_env

import sliding_puzzles
from config import parse_configs, seed_everything


if __name__ == "__main__":
    configs = parse_configs("sb3")
    seed_everything(configs["seed"])

    gym.logger.set_level(40)

    env = make_vec_env(
        "SlidingPuzzle-v0",
        n_envs=configs["n_envs"],
        seed=configs["seed"],
        env_kwargs=configs["env"],
        monitor_dir=f"runs/{configs['run_id']}/logs",
        monitor_kwargs={"info_keywords": ("is_success",)},
    )
    model = PPO(
        configs["sb3"]["policy"],
        env,
        verbose=1,
        tensorboard_log=f"runs/{configs['run_id']}",
        device="cuda",
        seed=configs["seed"],
        **configs["sb3"]["config"],
    )

    model.learn(
        total_timesteps=configs["total_timesteps"],
        progress_bar=True,
        callback=callbacks.EvalCallback(
            env,
            eval_freq=1500,
            n_eval_episodes=5,
            deterministic=True,
            render=False,
            log_path=f"runs/{configs['run_id']}/eval_logs",
            best_model_save_path=f"runs/{configs['run_id']}/best_model",
            verbose=1,
        ),
    )

    model.save(f"runs/{configs['run_id']}/model")
