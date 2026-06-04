import pandas as pd

df = pd.read_csv("raw_data.csv")

# Missing Values

print(df.isnull())

df["name"] = df["name"].fillna("Unknown")

# Duplicate Handling

print(df.duplicated())

df = df.drop_duplicates()

# Transformation

df["tax"] = df["income"].apply(
    lambda x: 20 if x > 60000 else 10
)

df = df.assign(
    new_income=df["income"] * (df["tax"]/100)
)

# Sorting

df = df.sort_values(
    ["income","age"]
)

df = df.reset_index(drop=True)

# Export

df.to_csv(
    "cleaned_data.csv",
    index=False
)

print(df.head())
