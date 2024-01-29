#!/bin/bash

# 2x2
python train.py --seed 304 --env-w 2 --env-h 2 --env-shuffle-steps 8 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 420 --env-w 2 --env-h 2 --env-shuffle-steps 8 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 650 --env-w 2 --env-h 2 --env-shuffle-steps 8 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy

# 3x3
python train.py --seed 304 --env-w 3 --env-h 3 --env-shuffle-steps 18 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 420 --env-w 3 --env-h 3 --env-shuffle-steps 18 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 650 --env-w 3 --env-h 3 --env-shuffle-steps 18 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy

# 4x4
python train.py --seed 304 --env-w 4 --env-h 4 --env-shuffle-steps 32 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 420 --env-w 4 --env-h 4 --env-shuffle-steps 32 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 650 --env-w 4 --env-h 4 --env-shuffle-steps 32 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy

# 5x5
python train.py --seed 304 --env-w 5 --env-h 5 --env-shuffle-steps 50 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 420 --env-w 5 --env-h 5 --env-shuffle-steps 50 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
python train.py --seed 650 --env-w 5 --env-h 5 --env-shuffle-steps 50 --env-variation image --env-image-folder ./imgs/mnist --env-image-background "(255,0,0)" --policy CnnPolicy
