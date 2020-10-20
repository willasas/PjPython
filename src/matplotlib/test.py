from cmath import atan
from turtle import color

from matplotlib import lines
import matplotlib
from matplotlib.figure import Figure
from matplotlib.pyplot import subplots_adjust
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import Axes

# 创建画布
fig = plt.figure()
<Figure size 432x288 with 0 Axes >
# 创建subplot,221表示这是2行2列表格中的第1个图像
ax1 = fig.add_subplot(221)
# 现在常用以下方式创建画布和图像， 2，2表示这是一个2*2的画布，可以放置4个图像
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# plt.subplot的sharex和sharey参数可以指定所有的subplot使用相同的x，y轴刻度
# subplots_adjust方法调整间距
Figure.subplots_adjust(left=None, bottom=None, right=None,
                       top=None, wspace=None, hspace=None)

plt.plot(np.random.randn(30), color='g', linestyle='--', marker='o')
# 不带参数调用，显示当前参数；
plt.xlim()
