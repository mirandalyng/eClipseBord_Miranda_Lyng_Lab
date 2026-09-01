from fastapi import FastAPI

# importing both dataframes of the solar and lunar datasets
from backend.data_processing import solar_df, lunar_df

app = FastAPI()

# dict for the datasets
DATASETS = {
    "solar": solar_df,
    "lunar": lunar_df,
}


@app.get("/eclipse/{data}")
async def show_data(data: str):
    df = DATASETS.get(data)
    # had to set the limit lower for the data to be able to load on my computer
    return df.head(20).to_dict(orient="records")
