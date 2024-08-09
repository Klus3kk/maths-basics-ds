import pandas as pd 

df = pd.read_csv('data.csv', delimiter=",")

correlation = df.corr(method='pearson')
print(correlation)