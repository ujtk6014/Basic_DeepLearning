import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from pylab import *
#from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtGui import QIcon

#グラフの複数表示
a = [a for a in range(10)]
b = [-a for a in a]
fig = plt.figure(1) #(figsize=(2, 2))
mngr = plt.get_current_fig_manager()
# to put it into the upper left corner for example:
mngr.window.setGeometry(800,400,640,545) #(X(左から),Y(上から),W,H)
a = plt.plot(a)

plt.figure(figsize=(2, 2))
b = plt.plot(b)
plt.show()

# def main():
#     df = pd.DataFrame(np.random.randint(0,50,size=(1000,1)),columns=list('A'))
#     df2 = df[df['A']<=25]
#     df2 = df2.reset_index()
#     df2['diff'] = df2['index'].diff()

#     cnt = 0
#     df2['オレンジ'] = 0
#     for i in range(len(df)):
#         if df2['diff'].get(i,None) == 1.0:
#             cnt += 1
#             if cnt >= 5:
#                 df2.loc[i-5:i,'オレンジ'] = df2.loc[i-5:i,'index']
#         else:
#             cnt = 0
#     fig = plt.figure()
#     plt.gca().set_axisbelow(False)
#     plt.grid(b=None, which='both', axis='both',color='k')
#     plt.plot(df['A'],color='blue',lw=0.5)
#     plt.vlines(df2['index'],0,50,color='yellow')
#     plt.vlines(df2['オレンジ'],0,50,color='orange')
#     plt.show()

# if __name__ == '__main__':
#     main()