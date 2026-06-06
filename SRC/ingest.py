from ucimlrepo import fetch_ucirepo
import pandas as pd

# Hent datasæt
dataset = fetch_ucirepo(id=601)

# Features og targets
X = dataset.data.features
y = dataset.data.targets

# Kombiner til én dataframe
df = pd.concat([X, y], axis=1)

# Gem som CSV
df.to_csv("data/raw/ai4i_2020.csv", index=False)

print("CSV gemt!")

# vis datasættet
print(df.head())
