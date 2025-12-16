import pandas as pd

df = pd.read_csv("employees.csv")

# finding highest paid employee
highest_paid = df["salary"].max()
print(highest_paid)

# finding department with highest average salary
avg_salary = df.groupby("department")["salary"].mean()
highest_avg = avg_salary.sort_values(ascending=False).head(1)
print(highest_avg)

# finding employees that joined after 2021
df["joining_date"] = pd.to_datetime(df["joining_date"])
df["joining_year"] = df["joining_date"].dt.year
joined_after_2021 = df[df["joining_year"] > 2021]

print("Employees joined after 2021: ")
print(joined_after_2021[["name", "joining_year"]])