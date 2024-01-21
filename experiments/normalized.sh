#!/bin/bash

# ---- NORMALIZED

# 2x2
python train.py --seed 304 --env-w 2 --env-h 2
python train.py --seed 420 --env-w 2 --env-h 2
python train.py --seed 650 --env-w 2 --env-h 2

# 3x3
python train.py --seed 304 --env-w 3 --env-h 3
python train.py --seed 420 --env-w 3 --env-h 3
python train.py --seed 650 --env-w 3 --env-h 3

# 4x4
python train.py --seed 304 --env-w 4 --env-h 4
python train.py --seed 420 --env-w 4 --env-h 4
python train.py --seed 650 --env-w 4 --env-h 4

# 5x5
python train.py --seed 304 --env-w 5 --env-h 5
python train.py --seed 420 --env-w 5 --env-h 5
python train.py --seed 650 --env-w 5 --env-h 5