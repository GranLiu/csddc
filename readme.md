# Control System Design Program
*created by 刘雍熙 in April*

## 项目结构
├── src (source codes of this program)
│    ├── csddc.py (basic class of this program)
│    ├── caseA.py (approach A)
│    ├── caseB.py (approach B)
│    └── caseC.py (approach C)
│
├── pics (some figures when executed)
│    └── ```
│
├── bk (backup codes used for test and development)
│    └── ```
│
├── main.py (access of program)
│
└── readme.md (readme document)

## 开发环境
本程序基于python3.8版本，利用pycharm平台实现，主要使用了control与sympy功能包

## 项目功能
实现了基于最小相位系统的三种控制系统实现方法

## 效果展示
This is a program for control system design simulation
We have three different ways to do simulations, choose A, B, or C:
### case A
please input the gain part of the function:10
please input the zero part of the function:1
please input the pole part of the function:(1+s)*(1+5*s)*(1+10*s)
Your input function is:
             10
────────────────────────────
(s + 1)⋅(5⋅s + 1)⋅(10⋅s + 1)
please input the phase limitation: 60
please input the frequency limitation: 0.2
Please input the amplitude of input step signal: 6
Please input the error rate when time goes to infinity: 0.1
In case A, R1 should be:  8
We can see from the first figure the condition is not satisfied
From the calculation we can get R2:
  (s + 1)⋅(5⋅s + 1)⋅(10⋅s + 1)
───────────────────────────────
                2
(0.015625⋅s + 1) ⋅(400.0⋅s + 1)
The ultimate function should be:
               80
───────────────────────────────
                2
(0.015625⋅s + 1) ⋅(400.0⋅s + 1)
After design simulation, the wp is:  0.19999577462578352
And the phase margin is:  90.3724397152805
![avatar](../pics/Case_a_Figure_1.png)
![avatar](../pics/Case_a_Figure_2.png)
### case B
please input the gain part of the function:10
please input the zero part of the function:1
please input the pole part of the function:(1+s)*(1+5*s)*(1+10*s)
Your input function is:
             10
────────────────────────────
(s + 1)⋅(5⋅s + 1)⋅(10⋅s + 1)
please input the phase limitation: 60
please input the frequency limitation: 0.2
Please input the amplitude of input step signal: 6
In case B, R1 should be:  8
And R2 should be:
(s + 1)⋅(5⋅s + 1)⋅(10⋅s + 1)
────────────────────────────
             2
 (0.02⋅s + 1) ⋅(1.0⋅s + 1)
The ultimate function should be:
            80
─────────────────────────
            2
(0.02⋅s + 1) ⋅(1.0⋅s + 1)
After design simulation, the wp is:  79.9937497558403
And the phase margin is:  90.71621589619497
![avatar](../pics/Case_b_Figure_1.png)
![avatar](../pics/Case_b_Figure_2.png)
### Case C
please input the gain part of the function:10
please input the zero part of the function:1
please input the pole part of the function:(1+s)*(1+5*s)*(1+10*s)
Your input function is:
             10
────────────────────────────
(s + 1)⋅(5⋅s + 1)⋅(10⋅s + 1)
please input the phase limitation: 60
please input the frequency limitation: 0.2
R1 should be:
1
─
s
phase margin at condition_w:  -29.744878733866187
so it is impossible to just adjust the ur to satisfy the conditions
now we cancel the pole of G(s) in low frequency
R2 now is:  9.99999999999996*s + 1
phase margin at condition_w:  33.45903490936496
But the phase margin is not satisfied, we should adjust the wp
Now R2 is:
(5.00000000000001⋅s + 1)⋅(9.99999999999996⋅s + 1)
─────────────────────────────────────────────────
             0.999999999999999⋅s + 1
when frequency equals to wc, the phase margin is:  68.02575257013994
now the wp is:  2.0081903270569996 so we should adjust the wp to wc
The ultimate function should be:
             10
────────────────────────────
(s + 1)⋅(5⋅s + 1)⋅(10⋅s + 1)
After design simulation, the wp is:  0.19905100730450787
And the phase margin is:  67.48822866391856
![avatar](../pics/Case_c_Figure_1.png)
![avatar](../pics/Case_c_Figure_2.png)
![avatar](../pics/Case_c_Figure_3.png)
## 项目总结
代码基本实现了最小相位系统设计的三种基本方法，对零点极点为常规多项式的函数有较好的控制特性。但也存在些许不足：

1. 因为python实现机制的原因进行整数除法时并不精准
2. 缺少迭代检查，实现状况较理想的情况下功能齐全，没有二次补偿后条件还不满足的问题