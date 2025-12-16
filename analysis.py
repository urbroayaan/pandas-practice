import pandas as pd

df = pd.read_csv("employees.csv")

# df.head() - returns first 5 rows
# df.shape -  returns (rows, columns)

# df.info() - describes all table header info with datatypes, memory allocation per head and total memory usage
# df.describe() - provides statistical analysis of the table data

names = df["name"]
subset = df[["name", "department", "salary"]]
print(names.head())
print(subset.head())
