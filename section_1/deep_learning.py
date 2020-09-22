import math
import numpy as np
#from matplotlib import pyplot
import matplotlib.pyplot as plt

"""
#matplotlibの使い方　例１
pi = math.pi

x = np.linspace(0, 2*pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)  #新たにcosを計算

pyplot.plot(x, sin_y, label='sin')
pyplot.plot(x, cos_y, label='cos')  #cosの値をプロット

#グラフタイトル
pyplot.title('Sin And Cos Graph')

#グラフの軸
pyplot.xlabel('X-Axis')
pyplot.ylabel('Y-Axis')

#グラフの凡例
pyplot.legend()

pyplot.show()
"""

"""
#p.18
#matplotlibの使い方　例２ 
x =  np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label = "sin")
plt.plot(x,y2, linestyle = "--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
"""
#p.19
from matplotlib.image import imread
img = imread('lene.png')
plt.imshow(img)
plt.show()


