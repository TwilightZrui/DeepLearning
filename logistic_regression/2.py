# coding: utf-8
import matplotlib.pyplot as plt 
import numpy as np 
X = np.array([[0,1,2,3]]).T 
y = np.array([0,1,2,3]).T 
theta1 = np.array([[0,0]]).T 
theta2 = np.array([[0, 0.5]]).T
theta3 = np.array([[0, 1]]).T


X_size = X.shape
X_0 = np.ones((X_size[0],1))
X_with_x0 = np.concatenate((X_0, X), axis = 1)

h1 = np.dot(X_with_x0,theta1)
h2 = np.dot(X_with_x0, theta2)
h3 = np.dot(X_with_x0, theta3)

plt.plot(X, y, 'rx', label='y')
plt.plot(X, h1, 'b', label='h1, theta_1=0')
plt.plot(X, h2, 'm', label='h2, theta_1=0.5')
plt.plot(X, h3, 'g', label='h3, theta_1=1')
plt.xlabel('X')
plt.ylabel('y/h')
plt.axis([-0.1, 4.5, -0.1, 4.5])
plt.legend(loc='upper left')
# plt.savefig('liner_gression_error.png', dpi=200) 
plt.show()

def calcu_cost(theta, X, y):
    m = X.shape[0]
    X_0 = np.ones((m, 1))
    X_with_x0 = np.concatenate((X_0, X), axis = 1)
    h = np.dot(X_with_x0, theta)
    cost = np.dot(((h - y).T , (h - y)/(2*m))