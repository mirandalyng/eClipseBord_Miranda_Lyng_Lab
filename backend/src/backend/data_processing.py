import pandas as pd
from backend.constants import DATA_PATH

# creating dataframes for both datasets
solar_df = pd.read_csv(DATA_PATH / "solar.csv")

lunar_df = pd.read_csv(DATA_PATH / "lunar.csv")

# fill missing values with 0
solar_df["Path Width (km)"] = solar_df["Path Width (km)"].fillna(0)
solar_df["Central Duration"] = solar_df["Central Duration"].fillna(0)
