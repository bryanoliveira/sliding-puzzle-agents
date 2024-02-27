#!/bin/bash

# 2x2
python train_ray.py -c ray_ppo_image --seed 304 --env--w 2 --env--h 2 --env--shuffle-steps 8 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 420 --env--w 2 --env--h 2 --env--shuffle-steps 8 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 650 --env--w 2 --env--h 2 --env--shuffle-steps 8 --env--image-folder ./imgs/imagenet-1k

# 3x3
python train_ray.py -c ray_ppo_image --seed 304 --env--w 3 --env--h 3 --env--shuffle-steps 18 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 420 --env--w 3 --env--h 3 --env--shuffle-steps 18 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 650 --env--w 3 --env--h 3 --env--shuffle-steps 18 --env--image-folder ./imgs/imagenet-1k

# 4x4
python train_ray.py -c ray_ppo_image --seed 304 --env--w 4 --env--h 4 --env--shuffle-steps 32 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 420 --env--w 4 --env--h 4 --env--shuffle-steps 32 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 650 --env--w 4 --env--h 4 --env--shuffle-steps 32 --env--image-folder ./imgs/imagenet-1k

# 5x5
python train_ray.py -c ray_ppo_image --seed 304 --env--w 5 --env--h 5 --env--shuffle-steps 50 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 420 --env--w 5 --env--h 5 --env--shuffle-steps 50 --env--image-folder ./imgs/imagenet-1k
python train_ray.py -c ray_ppo_image --seed 650 --env--w 5 --env--h 5 --env--shuffle-steps 50 --env--image-folder ./imgs/imagenet-1k