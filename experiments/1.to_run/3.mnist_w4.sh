#!/bin/bash

# 2x2
python train_ray.py -c ray_ppo --seed 594 --env--w 4 --total-timesteps 8000000 --env--variation image --env--image-folder mnist
python train_ray.py -c ray_ppo --seed 267 --env--w 4 --total-timesteps 8000000 --env--variation image --env--image-folder mnist
python train_ray.py -c ray_ppo --seed 769 --env--w 4 --total-timesteps 8000000 --env--variation image --env--image-folder mnist