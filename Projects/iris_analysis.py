import pandas as pd

# Load Dataset

df=pd.read_csv("IRIS.csv")

#Display first 10 rows:
df.head(10)

#Display shape and datatype:
df.shape
df.info()

#Display summary statics:
df.describe()

#Select those rows where petal length > 4.5 and species = "Iris-virginica":
df.query("petal_length > 4.5 & species == 'Iris-virginica'")

#Group by species and compute avg sepal length  max petal width and std_dev of sepal width:
df.groupby("species").agg(
    avg_sepal_length=("sepal_length","mean"),
    max_petal_width=("petal_width","max"),
    std_dev_sepal_width=("sepal_width","std")
)

#create a new column  petal ratio = petal_length/petal_width 
df=df.assign(petal_ratio = df["petal_length"]/df["petal_width"])

#For each species find the avg petal _ratio:
df.groupby("species")["petal_ratio"].mean()
