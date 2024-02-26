import argparse
import pickle
import time
import os
import yaml

import ray
from ray import tune
from ray.rllib.env.base_env import BaseEnv
from ray.rllib.policy.policy import Policy
from gymnasium.wrappers import EnvCompatibility
import sliding_puzzles


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help="model run id")
    parser.add_argument("-p", "--path", help="experiment path")
    parser.add_argument("-c", "--checkpoint", help="checkpoint number")
    args = parser.parse_args()

    experiment_path = f"runs/{args.model}" if args.path is None else args.path

    with open(f"{experiment_path}/configs.yaml", "r") as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)

    env = sliding_puzzles.make(
        render_mode="human",
        **configs["env"],
        invalid_move_reward=-1,
    )

    obs, info = env.reset()
    terminated = False
    truncated = False

    # -- ray stuff

    ray.init(ignore_reinit_error=True)

    ray_experiment_path = sorted(
        [
            f"{experiment_path}/{folder}"
            for folder in os.listdir(experiment_path)
            if os.path.isdir(f"{experiment_path}/{folder}")
        ]
    )[-1]
    checkpoint = sorted(
        [
            f"{ray_experiment_path}/{folder}"
            for folder in os.listdir(ray_experiment_path)
            if os.path.isdir(f"{ray_experiment_path}/{folder}") and folder != "wandb"
        ]
    )[-1] if args.checkpoint is None else f"{ray_experiment_path}/checkpoint_{str(args.checkpoint).zfill(6)}"
    print("Loading checkpoint:", checkpoint)
    agent = Policy.from_checkpoint(checkpoint)
    policy = agent[list(agent.keys())[0]]
    # agent.restore(checkpoint)

    while True:
        while not (terminated or truncated):
            action, *_ = policy.compute_single_action(obs, explore=True)
            print(action)
            obs, reward, terminated, truncated, info = env.step(action)
            print(obs)
            print(terminated, truncated, reward)
            env.render()
            time.sleep(0.5)

        input("Press Enter to continue...")
        obs, info = env.reset()
        terminated = False
        truncated = False
