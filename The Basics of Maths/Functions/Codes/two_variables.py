from sympy import *
from sympy.plotting import plot3d

x,y = symbols('x y')
f = 6*x + 2*y + 1
plot3d(f)