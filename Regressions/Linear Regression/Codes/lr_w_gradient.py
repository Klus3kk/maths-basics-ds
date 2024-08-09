import pandas as pd 

points = list(pd.read_csv('data.csv').itertuples())

m = 0.0
b = 0.0

L = .001

it = 100_000

n = float(len(points))

# Straight Gradient
for i in range(it):
    D_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in points)
    D_b = sum(2 * ((m * p.x + b) - p.y) for p in points)
    
    m -= L* D_m
    b -= L * D_b
    
print("y = {0}x + {1}".format(m,b))    