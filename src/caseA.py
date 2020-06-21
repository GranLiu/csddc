from src.csddc import *
from functools import reduce

"""
类case_a为Csddc的子类，对应于lecture中的case a
"""


class case_a(Csddc):
    def __init__(self):
        """
        创建对象时的初始化
        """
        super().__init__()
        self.in_ap = None
        self.ur = None
        self.error = None

    def get_ur(self):
        """
        得到 case a 中对应的R1的增益值
        """
        a = solve(self.in_ap / (1 + u * self.gain) - self.error, u)
        self.ur = int(a[0] + 3)

    def case_a_run(self):
        """
        按步骤进行 case a 的执行
        """
        self.in_sys()
        self.set_conditions()
        self.in_ap = float(input("Please input the amplitude of input step signal: "))
        self.error = float(input("Please input the error rate when time goes to infinity: "))
        self.get_ur()
        print("In case A, R1 should be: ", self.ur)
        self.expr1 = self.ur * self.expr1
        self.expr_to_sys(self.expr1, self.expr2)
        self.outs_sys()
        plt.figure(1)
        bode(self.sys)
        if self.wp < self.condition_w or self.pm < self.condition_phs:
            print("We can see from the first figure the condition is not satisfied")
            poles = pole(self.sys)
            wl = self.condition_w / (self.gain * self.ur)
            wh = pow(abs(1 / reduce(lambda x, y: x * y, poles)) / (1 / wl), -len(poles) + 1)
            self.R2up = self.expr2
            self.R2low = (1 + s / wl) * pow((1 + s / wh), len(poles) - 1)
            print("From the calculation we can get R2: ")
            pprint(self.R2up / self.R2low)
            self.expr = self.expr1 / self.R2low
            self.expr_to_sys(self.expr1, self.R2low)
            print("The ultimate function should be: ")
            pprint(self.expr)
            plt.figure(2)
            bode(self.sys)
            self.outs_sys()
            print("After design simulation, the wp is: ", self.wp)
            print("And the phase margin is: ", self.pm)
        plt.show()
