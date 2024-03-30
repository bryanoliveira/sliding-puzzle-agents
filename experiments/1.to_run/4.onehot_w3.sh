#!/bin/bash

# 2x2
python train_ray.py -c ray_ppo --seed 594 --env--w 3 --total-timesteps 3000000
python train_ray.py -c ray_ppo --seed 267 --env--w 3 --total-timesteps 3000000
python train_ray.py -c ray_ppo --seed 769 --env--w 3 --total-timesteps 3000000