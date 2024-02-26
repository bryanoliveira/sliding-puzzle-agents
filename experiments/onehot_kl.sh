#!/bin/bash

# 2x2
python train.py --seed 304 --env-w 2 --env-h 2 --env-shuffle-steps 8 --env-variation onehot --target-kl 0.2
python train.py --seed 420 --env-w 2 --env-h 2 --env-shuffle-steps 8 --env-variation onehot --target-kl 0.2
python train.py --seed 650 --env-w 2 --env-h 2 --env-shuffle-steps 8 --env-variation onehot --target-kl 0.2

# 3x3
python train.py --seed 304 --env-w 3 --env-h 3 --env-shuffle-steps 18 --env-variation onehot --target-kl 0.2
python train.py --seed 420 --env-w 3 --env-h 3 --env-shuffle-steps 18 --env-variation onehot --target-kl 0.2
python train.py --seed 650 --env-w 3 --env-h 3 --env-shuffle-steps 18 --env-variation onehot --target-kl 0.2