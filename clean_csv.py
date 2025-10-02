import pandas as pd

# Load the dataset (replace 'input.csv' with your file)
df = pd.read_csv("input.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Drop rows with missing values
df = df.dropna()

# Rename columns (example: change 'old_name' to 'new_name')
df = df.rename(columns={"old_name": "new_name"})

# Save the cleaned dataset
df.to_csv("output_clean.csv", index=False)

print(" Data cleaned and saved to output_clean.csv")
