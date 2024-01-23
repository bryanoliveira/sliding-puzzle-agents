#!/bin/bash

# 2x2
python train.py --seed 304 --env-w 2 --env-h 2 --env-shuffle-steps 8
python train.py --seed 420 --env-w 2 --env-h 2 --env-shuffle-steps 8
python train.py --seed 650 --env-w 2 --env-h 2 --env-shuffle-steps 8

# 3x3
python train.py --seed 304 --env-w 3 --env-h 3 --env-shuffle-steps 18
python train.py --seed 420 --env-w 3 --env-h 3 --env-shuffle-steps 18
python train.py --seed 650 --env-w 3 --env-h 3 --env-shuffle-steps 18

# 4x4
python train.py --seed 304 --env-w 4 --env-h 4 --env-shuffle-steps 32
python train.py --seed 420 --env-w 4 --env-h 4 --env-shuffle-steps 32
python train.py --seed 650 --env-w 4 --env-h 4 --env-shuffle-steps 32

# 5x5
python train.py --seed 304 --env-w 5 --env-h 5 --env-shuffle-steps 50
python train.py --seed 420 --env-w 5 --env-h 5 --env-shuffle-steps 50
python train.py --seed 650 --env-w 5 --env-h 5 --env-shuffle-steps 50