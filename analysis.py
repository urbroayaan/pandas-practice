import pandas as pd

df = pd.read_csv("employees.csv")

# df.head() - returns first 5 rows
# df.shape -  returns (rows, columns)

# df.info() - describes all table header info with datatypes, memory allocation per head and total memory usage
# df.describe() - provides statistical analysis of the table data

# names = df["name"] - selecting singular column
# subset = df[["name", "department", "salary"]] - selecting multiple columns by passing list

# high_salary = df[df["salary"] > 90000] - single condition
# it_emp = df[df["department"] == "IT"] - single condition
# it_high_paid = df[(df["department"] == "IT") & (df["salary"] > 90000)] - multiple condition

# df.isnull() - boolean table representation of all NULL items
# df.isnull().sum() - summed table showing number of NULL items
# df["age"] = df["age"].fillna(df["age"].mean()) - replaces NaN values within a column or table to specified value

df["bonus"] = df["salary"] * 0.10
df["tax"] = df["salary"] * 0.05
df["salary_after_tax"] = df["salary"] - df["tax"]

print(df.head())
