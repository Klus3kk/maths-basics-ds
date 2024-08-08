from sympy import *

x = symbols('x')
f = 1 / x

r = limit(f, x, oo)
print(r)