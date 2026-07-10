import pandas as pd

url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"

df = pd.read_csv(url)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nGENERALIZATIONS ABOUT THE DATASET")
print("""
1. The dataset contains historical CO2 emission data for different countries.
2. Each row represents one country in a particular year.
3. Higher population generally leads to higher CO2 emissions.
4. Countries with higher GDP usually produce more CO2 because of industrial activities.
5. Higher energy consumption per person generally increases CO2 emissions.
6. Coal, oil, and gas are the major contributors to total CO2 emissions.
7. Cement production contributes to industrial CO2 emissions.
8. Methane emissions are commonly associated with agriculture and livestock.
""")

print("\nRELATIONSHIP BETWEEN FEATURES")
print("""
Country -> Identifies the nation.
Year -> Indicates the observation year.
Population -> Larger population often increases energy demand.
GDP -> Higher GDP is usually related to higher industrial emissions.
Energy_per_capita -> More energy consumption usually increases CO2.
Coal_CO2 + Oil_CO2 + Gas_CO2 -> Major sources of Total CO2.
Cement_CO2 -> Related to construction activities.
Methane -> Related to agriculture and livestock.
""")

print("\nMissing Values")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
df["country"] = df["country"].fillna("Unknown")

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nTotal Countries")
print(df["country"].nunique())

print("\nYear Range")
print(df["year"].min(), "-", df["year"].max())

print("\nTop 10 Countries by Average CO2")
top10 = (
    df.groupby("country")["co2"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print(top10)

print("\nAverage Population")
print(df["population"].mean())

print("\nAverage GDP")
print(df["gdp"].mean())

print("\nAverage Energy Per Capita")
print(df["energy_per_capita"].mean())

print("\nCorrelation Matrix")
correlation = df[numeric_columns].corr()
print(correlation)

df.to_csv("cleaned_sustainability_dataset.csv", index=False)

print("\nSUMMARY")
print("""
1. Imported the sustainability dataset using Pandas.
2. Explored the dataset using head, tail, shape, columns, info, and describe.
3. Studied the relationship between different features.
4. Checked missing values.
5. Filled missing numerical values using the median.
6. Filled missing country names with 'Unknown'.
7. Performed analysis such as total countries, year range, average values, and top CO2 emitting countries.
8. Generated the correlation matrix.
9. Saved the cleaned dataset as 'cleaned_sustainability_dataset.csv'.
10. The dataset is now cleaned and ready for further analysis or visualization.
""")
