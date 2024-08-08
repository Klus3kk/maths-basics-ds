from sympy import *

n = symbols('n')

f = (1 + (1/n))**n

r = limit(f, n, oo)

print(r)