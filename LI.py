#线性插值与样条插值

'''
样例1:某电学元件的电压数据记录在0~2.25πA范围
与电流关系满足正弦函数，分别用线性插值和
样条插值方法给出经过数据点的数值逼近函数曲线。
'''

from cProfile import label
import numpy as np
import pylab as pl
from scipy import interpolate
import matplotlib.pyplot as plt

#原本的图像
x = np.linspace(0,2*np.pi+np.pi/4,10)
y = np.sin(x)

#新的
x_predicted = np.linspace(0,2*np.pi+np.pi/4,100)
f_linear = interpolate.interp1d(x,y)
tck = interpolate.splrep(x,y)
y_bspline = interpolate.splev(x_predicted,tck)

#可视化

plt.xlabel(u'安倍/A')
plt.ylabel(u'伏特/V')
plt.plot(x,y,"o",label=u"原始数据")
plt.plot(x_predicted,f_linear(x_predicted),label = u"线性插值")
plt.plot(x_predicted, y_bspline,label = u"B-spline插值")

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

pl.legend()
pl.show()