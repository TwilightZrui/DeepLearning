import numpy as np 
import matplotlib.pylab as plt  
from mpl_toolkits.mplot3d import Axes3D

def _numerical_gradient_no_batch(f,x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
