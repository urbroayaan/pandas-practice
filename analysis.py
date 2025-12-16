import pandas as pd

df = pd.read_csv("employees.csv")

# df.head() - returns first 5 rows
# df.shape -  returns (rows, columns)

print(df.info())
print(df.describe())
