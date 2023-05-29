import pandas as pd

# Create a sample dataframe
data = {
    'Name': ['John', 'Emma', 'Mike', 'Emily', 'David'],
    'Age': [28, 24, 35, 29, 32],
    'City': ['New York', 'London', 'Paris', 'Sydney', 'Tokyo'],
    'Salary': [50000, 60000, 55000, 70000, 45000]
}

df = pd.DataFrame(data)

# Display the dataframe
print("Original DataFrame:")
print(df)
print()

# Get basic statistics of the numeric columns
print("Basic Statistics:")
print(df.describe())
print()

# Sort the dataframe by Age in ascending order
sorted_df = df.sort_values('Age')
print("Sorted DataFrame by Age:")
print(sorted_df)
print()
