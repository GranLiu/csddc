from sympy import Symbol, sympify, Poly, solve, pprint
from control import *
import matplotlib.pyplot as plt

s = Symbol('s')
u = Symbol('u')


"""
类Csddc为所有case的基类，其成员变量包含了三种情况共有的成员
"""
class Csddc(object):
    def __init__(self):
        """
        创建对象时的初始化
        """
        self.condition_w = None
        self.condition_phs = None
        self.gain = None
        self.expr1 = None
        self.expr2 = None
        self.expr = None
        self.sys = None
        self.gm = None
        self.pm = None
        self.wg = None
        self.wp = None
        self.R1 = None
        self.R2up = None
        self.R2low = None

    def in_sys(self):
        """
        本函数进行系统函数，将函数不同部分从控制台输入并存储
        """
        self.gain = int(input("please input the gain part of the function:"))
        zeros = sympify(input("please input the zero part of the function:"))
        self.expr1 = self.gain * zeros
        self.expr1 = sympify(self.expr1)
        self.expr2 = sympify(input("please input the pole part of the function:"))
        self.expr = self.expr1 / self.expr2
        print("Your input function is: ")
        pprint(self.expr)
        pass

    def set_conditions(self):
        """
        本函数进行系统要求的初始化，将共有性能要求从控制台输入
        """
        self.condition_phs = float(input("please input the phase limitation: "))
        self.condition_w = float(input("please input the frequency limitation: "))
        pass

    def expr_to_sys(self, expr1, expr2):
        """
        本函数分别输入函数的分子与分母，生成对应的系统变换
        :param expr1: 函数的分子
        :param expr2: 函数的分母
        """
        sy1 = Poly(expr1, s).all_coeffs()
        sy2 = Poly(expr2, s).all_coeffs()
        a = list(map(int, sy1))
        b = list(map(int, sy2))
        sys_tf = tf(a, b)
        self.sys = ss(sys_tf)
        pass

    def outs_sys(self):
        """
        本函数得到系统的性能并存储于类成员中
        """
        self.gm, self.pm, self.wg, self.wp = margin(self.sys)
