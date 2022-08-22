# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

net = TwoLayerNet(input_size = 784, hidden_size = 100, output_size = 10)

x = np.random.rand(100, 784)
net.predict(x)
t = np.random.rand(100,10)
 
grad =  net.gradient(x,t)