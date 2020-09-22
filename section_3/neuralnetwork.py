import numpy as np
import matplotlib.pylab as plt

def step_func(x):
    return np.array(x > 0,dtype = np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

x_min = -5
x_max = 5
y_min = -0.1
y_max = 1.1
x1 = np.arange(x_min, x_max, 0.1)
#x2 = np.arange(-3.0, 3.0, 0.1)

y1 = step_func(x1)
y2 = sigmoid(x1)
y3 = relu(x1)
plt.plot(x1,y1,label = 'step')
plt.plot(x1,y2,linestyle = "--",label = 'sigmoid')
#plt.plot(x1,y3,linestyle = 'dashdot',label = 'ReLU')
plt.legend()
plt.ylim(y_min,y_max)
plt.xlim(x_min,x_max)
plt.show()
