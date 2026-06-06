import pandas as pd

df = pd.read_csv("raw/ai4i_2020.csv")

df["temperature_difference"] = (
    df["Process temperature"]
    - df["Air temperature"]
)

df["wear_per_torque"] = (
    df["Tool wear"]
    / df["Torque"]
)

df.to_csv(
    "data/processed/ai4i_processed.csv",
    index=False
)

machine_summary = (
    df.groupby("Type")
      .agg({
          "Machine failure":"sum",
          "Torque":"mean",
          "Tool wear":"mean"
      })
)
df.to_csv(
    "data/processed/machine_summary.csv",
    index=False
)