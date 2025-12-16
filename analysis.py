import pandas as pd

df = pd.read_csv("employees.csv")

# Preview the dataset to understand structure before making changes
# df.head()

# Check dataset size (rows, columns) before updates
# df.shape

# Review column names, data types, and memory usage
# df.info()

# Generate statistical summary for numeric columns
# df.describe()

# Select required columns for analysis
# subset = df[["name", "department", "salary"]]

# Filter employees with salary greater than 90,000
# high_salary = df[df["salary"] > 90000]

# Filter employees belonging to IT department
# it_emp = df[df["department"] == "IT"]

# Filter IT employees earning more than 90,000
# it_high_paid = df[(df["department"] == "IT") & (df["salary"] > 90000)]

# Identify missing values in the dataset
# df.isnull()

# Count missing values per column
# df.isnull().sum()

# Fill missing age values with average age (data cleaned before saving)
df["age"] = df["age"].fillna(df["age"].mean())

# Add bonus column calculated from salary
df["bonus"] = df["salary"] * 0.10

# Add tax column calculated from salary
df["tax"] = df["salary"] * 0.05

# Add final salary after tax deduction
df["salary_after_tax"] = df["salary"] - df["tax"]

# Convert joining_date from string to datetime for consistency
df["joining_date"] = pd.to_datetime(df["joining_date"])

# Extract joining year for easier time-based analysis
df["joining_year"] = df["joining_date"].dt.year

# Save cleaned and updated dataset to a new CSV file
df.to_csv("updated_employees.csv", index=False)
