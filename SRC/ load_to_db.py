import pandas as pd
from sqlalchemy import create_engine

# Læs processed data
df = pd.read_csv("data/processed/ai4i_processed.csv")

# Forbind til PostgreSQL
engine = create_engine(
    "postgresql://dairy_user:dairy_password@localhost:5432/dairy_db"
)

# Upload tabel
df.to_sql(
    "machine_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data uploadet til PostgreSQL!")