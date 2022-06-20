import pandas as pd

data1 = pd.read_csv("C:/1234/S1234.csv", sep=';', encoding="UTF-8")
print(data1.head(10))
print("done")