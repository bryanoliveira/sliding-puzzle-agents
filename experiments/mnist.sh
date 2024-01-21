#!/bin/bash

# ---- MNIST

# 2x2
python train.py --seed 304 --env-w 2 --env-h 2 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 420 --env-w 2 --env-h 2 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 650 --env-w 2 --env-h 2 --env-variation image --env-image-folder ./imgs/mnist/trainingSet

# 3x3
python train.py --seed 304 --env-w 3 --env-h 3 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 420 --env-w 3 --env-h 3 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 650 --env-w 3 --env-h 3 --env-variation image --env-image-folder ./imgs/mnist/trainingSet

# 4x4
python train.py --seed 304 --env-w 4 --env-h 4 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 420 --env-w 4 --env-h 4 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 650 --env-w 4 --env-h 4 --env-variation image --env-image-folder ./imgs/mnist/trainingSet

# 5x5
python train.py --seed 304 --env-w 5 --env-h 5 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 420 --env-w 5 --env-h 5 --env-variation image --env-image-folder ./imgs/mnist/trainingSet
python train.py --seed 650 --env-w 5 --env-h 5 --env-variation image --env-image-folder ./imgs/mnist/trainingSet