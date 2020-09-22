"""
#p.25
def AND(x1,x2):
    w1,w2,theta = 0.5, 0.5, 0.7
    temp = x1*w1 + w2*x2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1
AND(0,0)
AND(1,0)
AND(0,1)
AND(1,1)
"""
#p.27
import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y
    

val = input('Enter the number 1:AND 2:NAND 3:OR 4:XOR > ')
if val == '1':
    print(AND(0,0))
    print(AND(1,0))
    print(AND(0,1))
    print(AND(1,1))
elif val == '2':
    print(NAND(0,0))
    print(NAND(1,0))
    print(NAND(0,1))
    print(NAND(1,1))
elif val == '3':
    print(OR(0,0))
    print(OR(1,0))
    print(OR(0,1))
    print(OR(1,1))
elif val == '4':
    print(XOR(0,0))
    print(XOR(1,0))
    print(XOR(0,1))
    print(XOR(1,1))


