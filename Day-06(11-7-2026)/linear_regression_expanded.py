
"""
20260713_linear_regression.py
GreenSkilling / Sustainability Assignment
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================
# Load Dataset
# ==========================
try:
    from google.colab import files
    uploaded = files.upload()
    filename = list(uploaded.keys())[0]
except:
    filename = input("Enter CSV filename: ")

df = pd.read_csv(filename)

print("="*60)
print("FIRST 5 ROWS")
print(df.head())

print("="*60)
print("DATASET INFORMATION")
print(df.info())

print("="*60)
print(df.describe())

print("="*60)
print("MISSING VALUES")
print(df.isnull().sum())

print("="*60)
print("DUPLICATES :", df.duplicated().sum())

df.drop_duplicates(inplace=True)

# Handle Missing Values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# Feature Engineering
df["Total Renewable Power"] = (
    df["Installed - Bio-Mass Power"] +
    df["Installed - Small Hydro Power"] +
    df["Installed - Solar Power"] +
    df["Installed - Wind Power"] +
    df["Installed - Waste to Energy"]
)

df["Renewable Per Capita"] = (
    df["Total Renewable Power"] / df["Population"]
)

# Visualizations
sns.set(style="whitegrid")

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

df.hist(figsize=(14,10))
plt.savefig("histograms.png")
plt.close()

sns.pairplot(df.select_dtypes(include=np.number))
plt.savefig("pairplot.png")
plt.close()

for col in df.select_dtypes(include=np.number).columns:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.tight_layout()
    plt.savefig(f"boxplot_{col}.png")
    plt.close()

plt.figure(figsize=(14,5))
sns.countplot(data=df,x="Zone")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("zone_count.png")
plt.close()

plt.figure(figsize=(18,6))
sns.countplot(data=df,x="State")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("state_count.png")
plt.close()

# Encoding
df = pd.get_dummies(df, columns=["State","Zone"], drop_first=True)

# Scaling
target = "Installed - Solar Power"

X = df.drop(columns=[target])
y = df[target]

num_cols = X.select_dtypes(include=np.number).columns
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])

# Train/Test Split
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# Linear Regression
model = LinearRegression()
model.fit(X_train,y_train)

pred = model.predict(X_test)

mae = mean_absolute_error(y_test,pred)
mse = mean_squared_error(y_test,pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,pred)

print("\nMODEL EVALUATION")
print("MAE :",mae)
print("MSE :",mse)
print("RMSE:",rmse)
print("R2 Score:",r2)

joblib.dump(model,"20260713_linear_regression.pkl")
print("Model saved as 20260713_linear_regression.pkl")

print("""
INSIGHTS
--------
1. Missing numerical values -> Median.
2. Missing categorical values -> Mode.
3. Duplicates removed.
4. Total Renewable Power created through feature engineering.
5. Renewable Per Capita created for better comparison.
6. One-Hot Encoding applied on State and Zone.
7. StandardScaler applied to numerical columns.
8. Linear Regression predicts Installed Solar Power.
9. MAE shows average prediction error.
10. MSE penalizes larger errors.
11. RMSE is error in original units.
12. R² measures how well the model explains variance (closer to 1 is better).
""")
