import streamlit as st
import httpx
from backend.data_processing import solar_df, lunar_df
import pandas as pd
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"
IMAGES_DIR = Path(__file__).parents[3] / "images"


def get_data(DATASET):
    response = httpx.get(f"{BASE_URL}/eclipse/{DATASET}")
    data = response.json()
    return pd.DataFrame(data)


def show_dataset(df):
    st.markdown("### Eclipse Data")
    st.dataframe(df)


def main():
    st.markdown("# About Eclipses")

    st.info("An eclipse is an awe-inspiring celestial event that drastically changes "
            "the appearance of the two biggest objects we see in our sky: our Sun and Moon. "
            "On Earth, people can experience solar and lunar eclipses when Earth, the Moon, and the Sun line up. "
            "Safety is the number one priority when viewing a solar eclipse.  \n Source: NASA")

    st.markdown("### Solar vs Lunar Eclipse")

    st.image(IMAGES_DIR/"eclipse.jpg")
    st.markdown("### Choose Dataset")

    DATASET = st.selectbox("", ["solar", "lunar"])

    df = get_data(DATASET)

    show_dataset(df)


if __name__ == "__main__":
    main()
