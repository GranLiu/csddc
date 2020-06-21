from sympy import Symbol, sympify, simplify, pprint, expand, Poly, solve
from control import *
import matplotlib.pyplot as plt
u = Symbol('u')
solve(6.1 / (1 + u * 10.2) - 0.1, u)