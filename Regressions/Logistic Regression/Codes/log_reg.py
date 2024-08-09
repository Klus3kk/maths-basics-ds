import pandas as pd 
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.csv", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

model = LogisticRegression(penalty=None)
model.fit(X, Y)

print(model.coef_.flatten())
print(model.intercept_.flatten())