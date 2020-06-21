from scipy import signal
from pylab import *


def main():
    system = signal.lti([1, 1], [1, -5, 6])  # 类似tf函数，构建系统函数H(s)
    f = logspace(-2, 5)  # 取频率坐标，0.01Hz ~ 0.1MHz
    w = 2 * pi * f  # 取角频率
    w, mag, phase = signal.bode(system, w)  # 计算各参量, mag为幅频特性，phase为相频特性
    semilogx(f, phase)  # 绘制半对数坐标图（频率作为横轴采用对数坐标），将phase换成mag即为幅频特性曲线
    show()  # 很重要，如无此函数则不显示
