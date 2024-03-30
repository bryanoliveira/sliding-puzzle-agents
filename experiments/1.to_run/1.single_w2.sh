#!/bin/bash

# 2x2
python train_ray.py -c ray_ppo --seed 594 --env--w 2 --env--variation image --env--image-folder single
python train_ray.py -c ray_ppo --seed 267 --env--w 2 --env--variation image --env--image-folder single
python train_ray.py -c ray_ppo --seed 769 --env--w 2 --env--variation image --env--image-folder single