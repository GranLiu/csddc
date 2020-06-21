from src.csddc import *

"""
类case_b为Csddc的子类，对应于lecture中的case b
"""


class case_b(Csddc):
    def __init__(self):
        """
        创建对象时的初始化
        """
        super().__init__()
        self.in_ap = None
        self.ur = None
        self.error = 0.1

    def get_ur(self):
        """
        得到 case b 中对应的R1的增益值
        """
        a = solve(self.in_ap / (1 + u * self.gain) - self.error, u)
        self.ur = int(a[0] + 3)

    def case_b_run(self):
        """
        按步骤进行 case b 的执行
        """
        self.in_sys()
        self.set_conditions()
        self.in_ap = float(input("Please input the amplitude of input step signal: "))
        self.get_ur()
        print("In case B, R1 should be: ", self.ur)
        self.expr1 = self.ur * self.expr1
        self.expr_to_sys(self.expr1, self.expr2)
        self.outs_sys()
        plt.figure(1)
        bode(self.sys)
        if self.wp < self.condition_w or self.pm < self.condition_phs:
            poles = pole(self.sys)
            wl = -poles[0]
            wh = (-500 * poles[-1])
            self.R2up = self.expr2
            self.R2low = (1 + s / wl) * pow((1 + s / wh), len(poles) - 1)
            self.expr = self.expr1 / self.R2low
            self.expr_to_sys(self.expr1, self.R2low)
            print("And R2 should be: ")
            pprint(self.R2up / self.R2low)
            print("The ultimate function should be: ")
            pprint(self.expr)
            plt.figure(2)
            bode(self.sys)
            self.outs_sys()
            print("After design simulation, the wp is: ", self.wp)
            print("And the phase margin is: ", self.pm)
        plt.show()
