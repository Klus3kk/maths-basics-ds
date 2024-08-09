import random

def f(x):
    return (x - 3) ** 2 + 4

def dx_f(x):
    return 2*(x - 3)

# Learning Rate
L = 0.001

# The number of iterations
it = 100_000

# Random value
x = random.randint(-15,15)

for i in range(it):
    d_x = dx_f(x)
    x -= L * d_x
    
print(x, f(x))    
    