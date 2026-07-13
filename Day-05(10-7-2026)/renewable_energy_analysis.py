
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

try:
    from google.colab import files
    uploaded = files.upload()
    filename = list(uploaded.keys())[0]
except Exception:
    filename = input("Enter CSV filename: ")

df = pd.read_csv(filename)

print("First 5 Rows")
print(df.head())
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe(include="all"))
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

for c in df.columns:
    if df[c].dtype == "object":
        df[c] = df[c].fillna(df[c].mode()[0])
    else:
        df[c] = df[c].fillna(df[c].median())

if all(col in df.columns for col in [
    "Installed - Bio-Mass Power","Installed - Small Hydro Power",
    "Installed - Solar Power","Installed - Wind Power",
    "Installed - Waste to Energy"]):
    df["Total Renewable Power"] = (
        df["Installed - Bio-Mass Power"]+
        df["Installed - Small Hydro Power"]+
        df["Installed - Solar Power"]+
        df["Installed - Wind Power"]+
        df["Installed - Waste to Energy"]
    )

if "Population" in df.columns and "Total Renewable Power" in df.columns:
    df["Renewable Per Capita"] = df["Total Renewable Power"] / df["Population"]

num=df.select_dtypes(include=np.number).columns

plt.figure(figsize=(12,8))
sns.heatmap(df[num].corr(),annot=True,cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

df[num].hist(figsize=(15,10))
plt.tight_layout()
plt.show()

sns.pairplot(df[num])
plt.show()

for c in num:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[c])
    plt.title(c)
    plt.tight_layout()
    plt.show()

if "Zone" in df.columns:
    plt.figure(figsize=(8,4))
    sns.countplot(data=df,x="Zone")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if "State" in df.columns:
    plt.figure(figsize=(16,5))
    sns.countplot(data=df,x="State")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if all(c in df.columns for c in ["Zone","Installed - Solar Power"]):
    plt.figure(figsize=(8,4))
    sns.barplot(data=df,x="Zone",y="Installed - Solar Power")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if all(c in df.columns for c in ["Population","Installed - Solar Power","Zone"]):
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df,x="Population",y="Installed - Solar Power",hue="Zone")
    plt.tight_layout()
    plt.show()

if all(c in df.columns for c in ["Year","Installed - Solar Power"]):
    plt.figure(figsize=(8,5))
    sns.lineplot(data=df,x="Year",y="Installed - Solar Power")
    plt.tight_layout()
    plt.show()

cat=df.select_dtypes(include="object").columns
if len(cat)>0:
    df=pd.get_dummies(df,columns=list(cat),drop_first=True)

num=df.select_dtypes(include=np.number).columns
scaler=StandardScaler()
df[num]=scaler.fit_transform(df[num])

print("\nProcessed Data:")
print(df.head())

df.to_csv("processed_renewable_energy_dataset.csv",index=False)
print("\nSaved as processed_renewable_energy_dataset.csv")
