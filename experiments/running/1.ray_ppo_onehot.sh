#!/bin/bash

# 2x2
python train_ray.py -c ray_ppo --seed 304 --env--w 2 --env--h 2 --env--shuffle-steps 8 --env--variation onehot
python train_ray.py -c ray_ppo --seed 420 --env--w 2 --env--h 2 --env--shuffle-steps 8 --env--variation onehot
python train_ray.py -c ray_ppo --seed 650 --env--w 2 --env--h 2 --env--shuffle-steps 8 --env--variation onehot

# 3x3
python train_ray.py -c ray_ppo --seed 304 --env--w 3 --env--h 3 --env--shuffle-steps 18 --env--variation onehot
python train_ray.py -c ray_ppo --seed 420 --env--w 3 --env--h 3 --env--shuffle-steps 18 --env--variation onehot
python train_ray.py -c ray_ppo --seed 650 --env--w 3 --env--h 3 --env--shuffle-steps 18 --env--variation onehot

# 4x4
python train_ray.py -c ray_ppo --seed 304 --env--w 4 --env--h 4 --env--shuffle-steps 32 --env--variation onehot
python train_ray.py -c ray_ppo --seed 420 --env--w 4 --env--h 4 --env--shuffle-steps 32 --env--variation onehot
python train_ray.py -c ray_ppo --seed 650 --env--w 4 --env--h 4 --env--shuffle-steps 32 --env--variation onehot

# 5x5
python train_ray.py -c ray_ppo --seed 304 --env--w 5 --env--h 5 --env--shuffle-steps 50 --env--variation onehot
python train_ray.py -c ray_ppo --seed 420 --env--w 5 --env--h 5 --env--shuffle-steps 50 --env--variation onehot
python train_ray.py -c ray_ppo --seed 650 --env--w 5 --env--h 5 --env--shuffle-steps 50 --env--variation onehot