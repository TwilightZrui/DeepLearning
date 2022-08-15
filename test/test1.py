# coding: utf-8
# from cProfile import label
# from matplotlib.lines import _LineStyle
import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0,6,0.1) 
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label = "sin")
plt.plot(x,y2, linestyle="--", label = "cos")

plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()



# x = np.arange(0, 6, 0.1)
# y = np.sin(x)

# plt.plot(x, y)
# plt.show()


# class Man:
#     """
#     ls
#     """
#     def __init__(self, name):
#         self.name = name 
#         print("initilized!")
    
#     def hello(self):
#         print("Hello" + self.name + "!")
    
#     def goodbye(self):
#         print("good bye " + self.name + "!")

# m = Man("David")
# m.hello()
# m.goodbye()
# import matplotlib.pyplot as plt 
# from matplotlib.image import imread 

# img = imread('./dataset/lena.png')
# plt.imshow(img)

# plt.show()

# def myfunc(n):
#   return lambda a : a * n

# mytripler = myfunc(3) 

# print(mytripler(11))
# x = lambda a,b: a+b
# print(x(5,6))