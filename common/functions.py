# coding: utf-8
import numpy as np 

def identity_function(x):
    return x

def step_function(x):
    return np.array(x > 0, dtype = np.int)

def sigmod(x):
    return 1 / (1 + np.exp(-x))

def sigmod_grad(x):
    return (1 - sigmod(x)) * sigmod(x)
   
def relu(x):
    return np.maximum(0, x)

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis = 0)
        y = np.exp(x) / np.sum(np.exp(x), axis = 0)

    x =x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

#y[np.arange(batch_size), t]能抽出各个数据的正确街标签对应的神经网络的输出

def softmax_loss(X, t):
    y = softmax(X)     
    return cross_entropy_error(y , t)