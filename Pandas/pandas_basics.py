import pandas as pd
import numpy as np

# DataFrame from Dictionary

info = {
    "Name":["Aadi","Rohan","Mohan"],
    "Age":[20,19,23],
    "CGPA":[8,9.0,7.4]
}

df = pd.DataFrame(info)

print(df)

print(df.index)
print(df.columns)

# DataFrame from List

df2 = pd.DataFrame(
    [["Ram",20],["Sham",12],["Sita",90],["Geeta",78]],
    columns=["Name","Age"]
)

print(df2)

# DataFrame from NumPy Array

arr = np.array([
    [1,2,3,7],
    [4,5,6,8]
])

df3 = pd.DataFrame(arr,columns=["A","B","C","D"])

print(df3)

# Basic Selection

print(df["Name"])

print(df.loc[0])

print(df.iloc[0])
