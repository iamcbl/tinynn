import sys
import os
sys.path.append(os.getcwd())

import numpy as np
from typing import List

from core.train import train, evaluate
from core.nn import NeuralNet
from core.layers import Linear, Tanh
from core.data import DataIterator, BatchIterator
from core.optimizer import SGD, Adam, RMSProp, Momentum


def fizzbuzz_encode(x: int) -> List[int]:
    if x % 15 == 0:
        return [0, 0, 0, 1]
    elif x % 5 == 0:
        return [0, 0, 1, 0]
    elif x % 3 == 0:
        return [0, 1, 0, 0]
    else:
        return [1, 0, 0, 0]


def binary_encode(x: int) -> List[int]:
    return [x >> i & 1 for i in range(10)]


train_X = np.array([binary_encode(x) for x in range(101, 1024)])
train_Y = np.array([fizzbuzz_encode(x) for x in range(101, 1024)])

net = NeuralNet([
    Linear(input_size=10, output_size=50),
    Tanh(),
    Linear(input_size=50, output_size=4)
])

train(net, train_X, train_Y, num_epochs=3000, iterator=BatchIterator(batch_size=32), optimizer=Momentum(lr=1e-3))

test_X = np.array([binary_encode(x) for x in range(1, 101)])
test_Y = np.array([fizzbuzz_encode(x) for x in range(1, 101)])

evaluate(net, test_X, test_Y)
