from src.csddc import *

"""
类case_c为Csddc的子类，对应于lecture中的case c
"""


class case_c(Csddc):
    def __init__(self):
        """
        创建对象时的初始化
        """
        super().__init__()
        self.in_ap = None
        self.ur = 1
        self.error = None

    def case_c_run(self):
        """
        按步骤进行 case c 的执行
        """
        self.in_sys()
        self.set_conditions()
        self.expr1 = self.ur * self.expr1
        self.expr2 = self.expr2 * s
        self.R1 = self.ur / s
        print("R1 should be: ")
        pprint(self.R1)
        self.expr_to_sys(self.expr1, self.expr2)
        self.outs_sys()
        plt.figure(1)
        bode(self.sys)
        mag, phase, omega = freqresp(self.sys, [self.condition_w])
        poles = pole(self.sys)
        if phase[0][0][0] > 0:
            ph_mg = phase[0][0][0] / 3.1415926 * 180 - 360 + 180
        else:
            ph_mg = phase[0][0][0] / 3.1415926 * 180 + 180
        print("phase margin at condition_w: ", ph_mg)
        if ph_mg < self.condition_phs:
            print("so it is impossible to just adjust the ur to satisfy the conditions")
            print("now we cancel the pole of G(s) in low frequency")
            self.R2up = 1 + s * (-1 / poles[-1])
            print("R2 now is: ", self.R2up)
            self.expr1 = self.expr1 * self.R2up
            self.expr_to_sys(self.expr1, self.expr2)
            mag, phase, omega = freqresp(self.sys, [self.condition_w])
            if phase[0][0][0] > 0:
                ph_mg = phase[0][0][0] / 3.1415926 * 180 - 360 + 180
            else:
                ph_mg = phase[0][0][0] / 3.1415926 * 180 + 180
            print("phase margin at condition_w: ", ph_mg)
            if ph_mg < self.condition_phs:
                print("But the phase margin is not satisfied, we should adjust the wp")
                self.R2up = self.R2up * (1 + s * (-1 / poles[-2]))
                self.R2low = 1 + s * (-1 / poles[1])
                print("Now R2 is: ")
                pprint(self.R2up / self.R2low)
                self.expr1 = self.expr1 * (1 + s * (-1 / poles[-2]))
                self.expr2 = self.expr2 * self.R2low
                self.expr_to_sys(self.expr1, self.expr2)
                self.outs_sys()
                plt.figure(2)
                bode(self.sys)
                mag, phase, omega = freqresp(self.sys, [self.condition_w])
                if phase[0][0][0] > 0:
                    ph_mg = phase[0][0][0] / 3.1415926 * 180 - 360 + 180
                else:
                    ph_mg = phase[0][0][0] / 3.1415926 * 180 + 180
                print("when frequency equals to wc, the phase margin is: ", ph_mg)
                print("now the wp is: ", self.wp, "so we should adjust the wp to wc")
                self.R2low = mag[0][0][0]
                self.expr2 = self.expr2 * self.R2low
                self.expr_to_sys(self.expr1, self.expr2)
                print("The ultimate function should be: ")
                pprint(self.expr)
                self.outs_sys()
        print("After design simulation, the wp is: ", self.wp)
        print("And the phase margin is: ", self.pm)
        plt.figure(3)
        bode(self.sys)
        plt.show()
