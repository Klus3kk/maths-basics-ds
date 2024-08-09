# EXAMPLE TAKEN FROM THE BOOK!
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

# Import
df = pd.read_csv('data.csv', delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

# Fitting the line to the points
f = LinearRegression().fit(X,Y)

m = f.coef_.flatten()
b = f.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# Showing the graph
plt.plot(X, Y, 'o')
plt.plot(X, m*X+b)
plt.show()