# coding: utf-8
# import numpy as np
# import matplotlib.pyplot as plt
# def relu(x):
#     return np.maximum(0, x)
    
# x = np.arange(-3,3,0.1)
# y = relu(x)

# plt.plot(x,y)
# plt.show()

import os.path 
  
# Path 
path = '/home/twilight/project/learning/CNN_python/common/functions.py'
  
# Get the directory name   
# from the specified path 
dirname = os.path.dirname(os.path.abspath(__file__)) 
  
# Print the directory name   
print(os.path.abspath(__file__)) 

