#数値微分
import numpy as np
import matplotlib.pylab as plt


def num_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h) )/ (2*h)

def func_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0.0,20.0,0.1)
y = func_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
#plt.show()

a = num_diff(func_1, 5)
print(a)
b = num_diff(func_1, 10)
print(b)


