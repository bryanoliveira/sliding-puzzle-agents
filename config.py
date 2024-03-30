import argparse
import datetime
import os
import random
import yaml

import numpy as np


def update_flat_nested(d: dict, u: dict):
    """Update d with u's values.
    u's keys are flattened, so u["some__value"] corresponds to d["some"]["value"]
    """
    for k, v in u.items():
        if "__" in k:
            k, *rest = k.split("__")
            update_flat_nested(d.setdefault(k, {}), {"__".join(rest): v})
        elif isinstance(v, dict):
            update_flat_nested(d.setdefault(k, {}), v)
        elif v is not None:
            d[k] = v

    return d


def parse_configs(framework):
    # Create the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str, required=True)

    parser.add_argument("--experiment-name", type=str)
    parser.add_argument("--run-id", type=str)
    parser.add_argument("--disable-wandb", action="store_true")
    parser.add_argument("--wandb-project", type=str)
    parser.add_argument("--n-envs", type=int)

    parser.add_argument("--seed", type=int)
    parser.add_argument("--logdir", type=str)
    parser.add_argument("--checkpoint", type=str)

    parser.add_argument("--total-timesteps", type=int)
    parser.add_argument("--env--w", type=int)
    parser.add_argument("--env--h", type=int)
    parser.add_argument("--env--shuffle-steps", type=int)
    parser.add_argument("--env--sparse-rewards", action="store_true")
    parser.add_argument("--env--sparse-mode", type=str)
    parser.add_argument("--env--win-reward", type=int)
    parser.add_argument("--env--variation", type=str)
    parser.add_argument("--env--image-folder", type=str)
    parser.add_argument("--env--image-background", type=eval)
    # sb3
    parser.add_argument(
        "--sb3--policy",
        type=str,
        choices=["MlpPolicy", "CnnPolicy"],
    )
    # ray
    parser.add_argument("--ray--algorithm", type=str)
    parser.add_argument("--ray--config--num-workers", type=int)
    cl_configs = vars(parser.parse_args())

    # open base configs from cli
    if ".yaml" not in cl_configs["config"]:
        cl_configs["config"] = os.path.join("configs", cl_configs["config"] + ".yaml")
    with open(cl_configs["config"]) as f:
        base_configs = yaml.load(f, Loader=yaml.FullLoader)

    # create an update chain to allow for parent config inheritance
    # this chain will be parsed in reverse
    update_chain = [cl_configs, base_configs]
    # while current parent has a parent, add them to the chain
    while (
        "parent_config" in update_chain[-1]
        and update_chain[-1]["parent_config"] is not None
    ):
        parent_configs = yaml.load(
            open(
                os.path.join(
                    os.path.dirname(cl_configs["config"]),
                    update_chain[-1]["parent_config"] + ".yaml",
                )
            ),
            Loader=yaml.FullLoader,
        )
        update_chain.append(parent_configs)
    # get the first parent
    configs = update_chain.pop()
    # reverse the chain
    update_chain.reverse()
    # override each child config
    for override_configs in update_chain:
        configs = update_flat_nested(configs, override_configs)

    configs["framework"] = framework

    # create an experiment name if not provided
    if "run_id" not in configs or not configs["run_id"]:
        configs["run_id"] = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if "experiment_name" not in configs or not configs["experiment_name"]:
        configs["experiment_name"] = f"{configs['framework']}_{configs['env']['variation']}"
        if configs["env"]["variation"] == "image":
            configs[
                "experiment_name"
            ] += f"_{configs['env']['image_folder'].split('/')[-1]}"
        configs["experiment_name"] += f"_{configs['env']['w']}x{configs['env']['h']}"
        if configs["env"]["sparse_rewards"]:
            configs["experiment_name"] += f"_sparse_{configs['env']['sparse_mode']}"
        if (
            "ray" in configs
            and "algorithm" in configs["ray"]
            and configs["ray"]["algorithm"]
        ):
            configs["experiment_name"] += f"_{configs['ray']['algorithm']}"

    configs["run_id"] = f"{configs['run_id']}-{configs['experiment_name']}-{configs['seed']}"

    if (
        "env" in configs
        and "image_folder" in configs["env"]
        and configs["env"]["image_folder"]
    ):
        configs["env"]["image_folder"] = os.path.abspath(configs["env"]["image_folder"])

    # dump the configs
    os.makedirs(f"{configs['logdir']}/{configs['run_id']}", exist_ok=True)
    with open(f"{configs['logdir']}/{configs['run_id']}/configs.yaml", "w") as f:
        yaml.dump(configs, f)

    return configs


def seed_everything(seed: int):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    try:
        import tensorflow as tf

        tf.random.set_seed(seed)
    except ImportError:
        pass
    try:
        import torch

        torch.manual_seed(seed)
    except ImportError:
        pass
