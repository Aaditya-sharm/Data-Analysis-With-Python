mport pandas as pd

# Load Dataset
df=pd.read_csv("Titanic-Dataset.csv")

#Display only columns :Name,Sex,Age,Fare,Survived :
df[["Name","Sex","Age","Fare","Survived"]]

#Select passengers who are female and has fare > 30 :
df.query("Sex == 'female' & Fare > 30")

#Group by Pclass and compute survival rate , avg fare and avg age:
df.groupby("Pclass").agg(
    Survival_rate = ("Survived","mean"),
    avg_fare=("Fare","mean"),
    avg_age=("Age","mean")
)
