import pandas as pd
from backend.constants import DATA_PATH

# creating dataframes for both datasets
solar_df = pd.read_csv(DATA_PATH / "solar.csv")

lunar_df = pd.read_csv(DATA_PATH / "lunar.csv")
