# coding: utf-8
from mnist import load_mnist
import numpy as np
from two_layer_net import TwoLayerNet


(x_train, t_train),(x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

sample_size = 3
x_batch = x_train[:sample_size]
t_batch = t_train[:sample_size]

size = x_train.shape
print(size)
size1 = x_batch.shape
print(size1)

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

for key in grad_numerical.keys():
    diff = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )
    print(key + ":" + str(diff))