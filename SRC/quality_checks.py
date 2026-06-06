import pandas as pd

df = pd.read_csv("data/raw/ai4i_2020.csv")

print("Antal rækker:", len(df))
print("Antal kolonner:", len(df.columns))

print("\nManglende værdier:")
print(df.isnull().sum())

print("\nDatatyper:")
print(df.dtypes)

assert (df["Air temperature"] > 0).all()
assert (df["Process temperature"] > 0).all()
assert (df["Rotational speed"] > 0).all()

print("Alle quality checks bestået!")