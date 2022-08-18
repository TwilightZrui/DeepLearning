# https://www.cnblogs.com/picassooo/p/12563378.html
import matplotlib.pyplot as plt
x = list(range(1, 21))  # epoch array
loss = [2 / (i**2) for i in x]  # loss values array
plt.ion()
for i in range(1, len(x)):
    ix = x[:i]
    iy = loss[:i]
    plt.cla()
    plt.title("loss")
    plt.plot(ix, iy)
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.pause(0.5)
plt.ioff()
plt.show()