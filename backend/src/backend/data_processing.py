import pandas as pd
from backend.constants import DATA_PATH

# creating dataframes for both datasets
solar_df = pd.read_csv(DATA_PATH / "solar.csv")

lunar_df = pd.read_csv(DATA_PATH / "lunar.csv")

# fill missing values with missing
solar_df["Path Width (km)"] = solar_df["Path Width (km)"].fillna("missing")
solar_df["Central Duration"] = solar_df["Central Duration"].fillna("missing")

lunar_df["Partial Eclipse Duration (m)"] = lunar_df["Partial Eclipse Duration (m)"].fillna(
    "missing")
lunar_df[",Total Eclipse Duration (m)"] = lunar_df["Total Eclipse Duration (m)"].fillna(
    "missing")
