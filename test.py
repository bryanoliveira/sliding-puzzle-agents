import argparse
import time
import yaml

import gymnasium as gym
from stable_baselines3 import PPO

import sliding_puzzles


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help="model run id")
    args = parser.parse_args()

    with open(f"runs/{args.model}/configs.yaml", "r") as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)

    env = sliding_puzzles.make(
        render_mode="human",
        w=configs["env_w"],
        h=configs["env_h"],
        variation=configs["env_variation"],
        image_folder=configs["env_image_folder"],
        shuffle_steps=configs["env_shuffle_steps"],
    )

    obs, info = env.reset()
    terminated = False
    truncated = False

    model = PPO.load(f"runs/{args.model}/model", env=env)

    while True:
        while not (terminated or truncated):
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action.item())
            print(obs)
            print(terminated, truncated, reward)
            env.render()
            time.sleep(0.5)

        input("Press Enter to continue...")
        obs, info = env.reset()
        terminated = False
        truncated = False
