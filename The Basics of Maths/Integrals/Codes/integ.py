from sympy import *

x = symbols('x')

f = x**2 + 1
# Field between x=0 and x=1
field = integrate(f, (x, 0, 1))

print(field)