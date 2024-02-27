import random

import gymnasium as gym
import pprint
import ray
from ray import train, tune
from ray.tune.schedulers import PopulationBasedTraining

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--smoke-test", action="store_true", help="Finish quickly for testing"
    )
    args, _ = parser.parse_known_args()

    def create_env(config):
        import sliding_puzzles

        return gym.make("SlidingPuzzle-v0", **config)

    tune.registry.register_env("SlidingPuzzle", create_env)

    # Postprocess the perturbed config to ensure it's still valid
    def explore(config):
        # ensure we collect enough timesteps to do sgd
        if config["train_batch_size"] < config["sgd_minibatch_size"] * 2:
            config["train_batch_size"] = config["sgd_minibatch_size"] * 2
        # ensure we run at least one sgd iter
        if config["num_sgd_iter"] < 1:
            config["num_sgd_iter"] = 1
        return config

    hyperparam_mutations = {
        "lambda": lambda: random.uniform(0.9, 1.0),
        "gamma": lambda: random.uniform(0.9, 1.0),
        "clip_param": lambda: random.uniform(0.01, 0.5),
        "lr": [1e-3, 5e-4, 1e-4, 5e-5, 1e-5],
        "num_sgd_iter": lambda: random.randint(1, 30),
        "sgd_minibatch_size": lambda: random.randint(128, 16384),
        "train_batch_size": lambda: random.randint(2000, 160000),
    }

    pbt = PopulationBasedTraining(
        time_attr="time_total_s",
        perturbation_interval=120,
        resample_probability=0.25,
        # Specifies the mutations of these hyperparams
        hyperparam_mutations=hyperparam_mutations,
        custom_explore_fn=explore,
    )

    # Stop when we've either reached 100 training iterations or reward=300
    stopping_criteria = {"training_iteration": 100, "episode_reward_mean": 5}

    tuner = tune.Tuner(
        "PPO",
        tune_config=tune.TuneConfig(
            metric="episode_reward_mean",
            mode="max",
            scheduler=pbt,
            num_samples=1 if args.smoke_test else 20,
        ),
        param_space={
            "env": "SlidingPuzzle",
            "env_config": {
                "variation": "onehot",
                "w": 3,
                "h": 3,
                "shuffle_steps": 100,
                "sparse_rewards": False,
                "invalid_move_reward": -1,
            },
            "kl_coeff": 1.0,
            "num_workers": 4,
            "num_cpus": 1,  # number of CPUs to use per trial
            "num_gpus": 0,  # number of GPUs to use per trial
            "model": {"free_log_std": True},
            # These params are tuned from a fixed starting value.
            "lambda": 0.95,
            "gamma": 0.99,
            "clip_param": 0.2,
            "lr": 1e-4,
            # These params start off randomly drawn from a set.
            "num_sgd_iter": tune.choice([10, 20, 30]),
            "sgd_minibatch_size": tune.choice([128, 512, 2048]),
            "train_batch_size": tune.choice([10000, 20000, 40000]),
        },
        run_config=train.RunConfig(stop=stopping_criteria),
    )
    results = tuner.fit()

    best_result = results.get_best_result()

    print("Best performing trial's final set of hyperparameters:\n")
    pprint.pprint(best_result.config)

    print("\nBest performing trial's final reported metrics:\n")
    pprint.pprint(best_result)
