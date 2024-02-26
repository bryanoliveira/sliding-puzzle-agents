import unittest

import gymnasium as gym
import numpy as np

import ray
from ray.rllib.algorithms.dreamerv3 import dreamerv3
from ray.rllib.policy.sample_batch import DEFAULT_POLICY_ID
from ray.rllib.utils.numpy import one_hot
from ray.rllib.utils.test_utils import framework_iterator
from ray import tune

import sliding_puzzles

# Build a DreamerV3Config object.
config = (
    dreamerv3.DreamerV3Config()
    .training(
        # Keep things simple. Especially the long dream rollouts seem
        # to take an enormous amount of time (initially).
        batch_size_B=4,
        horizon_H=5,
        batch_length_T=16,
        model_size="nano",  # Use a tiny model for testing
        symlog_obs=True,
        use_float16=False,
    )
    .resources(
        num_learner_workers=2,  # Try with 2 Learners.
        num_cpus_per_learner_worker=1,
        num_gpus_per_learner_worker=0,
    )
)

num_iterations = 2
env = "SlidingPuzzle-v0"

config.environment(env, env_config={"variation": "onehot", "w": 3, "h": 3})
algo = config.build()
obs_space = algo.workers.local_worker().env.single_observation_space
act_space = algo.workers.local_worker().env.single_action_space
rl_module = algo.workers.local_worker().module

for i in range(num_iterations):
    results = algo.train()
    print(results)
