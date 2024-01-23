import argparse
import datetime
import os
import yaml

import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

import sliding_puzzles
from callbacks import SuccessRateCallback


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--run_id", type=str, default=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    )
    parser.add_argument(
        "--policy", type=str, default="MlpPolicy", choices=["MlpPolicy", "CnnPolicy"]
    )
    parser.add_argument("--total-timesteps", type=int, default=1000000)
    parser.add_argument("--env-w", type=int, default=2)
    parser.add_argument("--env-h", type=int, default=2)
    parser.add_argument("--env-shuffle-steps", type=int, default=5)
    parser.add_argument("--env-sparse-rewards", action="store_true")
    parser.add_argument("--env-sparse-mode", type=str, default="invalid_and_win")
    parser.add_argument("--env-win-reward", type=int, default=10)
    parser.add_argument("--env-variation", type=str, default="normalized")
    parser.add_argument("--env-image-folder", type=str, default="imgs/single")
    parser.add_argument("--n-envs", type=int, default=32)
    parser.add_argument("--n-steps", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    os.makedirs(f"runs/{args.run_id}", exist_ok=True)
    with open(f"runs/{args.run_id}/configs.yaml", "w") as f:
        yaml.dump(vars(args), f)
    configs = vars(args)

    np.random.seed(configs["seed"])
    gym.logger.set_level(40)

    env = make_vec_env(
        "SlidingPuzzle-v0",
        n_envs=configs["n_envs"],
        seed=configs["seed"],
        env_kwargs={
            "w": configs["env_w"],
            "h": configs["env_h"],
            "shuffle_steps": configs["env_shuffle_steps"],
            "sparse_rewards": configs["env_sparse_rewards"],
            "sparse_mode": configs["env_sparse_mode"],
            "win_reward": configs["env_win_reward"],
            "variation": configs["env_variation"],
            "image_folder": configs["env_image_folder"],
        },
        monitor_dir=f"runs/{configs['run_id']}/logs",
        monitor_kwargs={"info_keywords": ("is_success",)},
    )
    model = PPO(
        configs["policy"],
        env,
        verbose=1,
        tensorboard_log=f"runs/{configs['run_id']}",
        device="cuda",
        seed=configs["seed"],
        n_steps=configs["n_steps"],
    )

    model.learn(
        total_timesteps=configs["total_timesteps"],
        progress_bar=True,
        callback=SuccessRateCallback(),
    )

    model.save(f"runs/{configs['run_id']}/model")
