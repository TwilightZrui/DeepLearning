from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(- 3 , 3 , 0.25 )
y = np.arange(- 3 , 3 , 1 )
X, Y = np.meshgrid(x, y)
print(X.shape)
Z = np.sin(X) + np.cos(Y)

image = plt.figure()
ax = Axes3D(image)
ax.plot_wireframe(X,Y,Z) #<--- 在此处绘图

plt.show()
plt.savefig('3D.png', dpi=200)

#https://white-wheels.hatenadiary.org/entry/20100327/p3

