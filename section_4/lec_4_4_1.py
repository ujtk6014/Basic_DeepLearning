import numpy as np

def func_2(x):
    return np.sum(x**2)

def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x)
    #print(x.size)

    for idx in range(x.size):
        temp_val = x[idx]
        x[idx] = temp_val + h
        fxh1 = f(x)

        x[idx] = temp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = temp_val
    
    return grad

#勾配法を用いた勾配の計算
# a = numerical_gradient(func_2, np.array([3.0,4.0]))
# print(a)
# b = numerical_gradient(func_2, np.array([0.0,2.0]))
# print(b)

def gradient_decent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr*grad
    return x

init_x = np.array([-3.0,4.0])
x =gradient_decent(func_2,init_x=init_x, lr=0.1, step_num=100) 
print(x)

