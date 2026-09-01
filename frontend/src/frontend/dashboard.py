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


def lunar_data(df):
    st.markdown("### Lunar Eclipse Insights")

    df["Eclipse Type Simple"] = df["Eclipse Type"].str[0].map({
        "N": "Penumbral",
        "P": "Partial",
        "T": "Total",
    })

    st.bar_chart(df["Eclipse Type Simple"].value_counts(), color="#3F185B")

    df["Hours"] = pd.to_datetime(df["Eclipse Time"], format="%H:%M:%S").dt.hour
    hour_eclipse = df["Hours"].value_counts().sort_index()

    st.markdown("### Eclipses Hourly")
    st.bar_chart(hour_eclipse, color="#3F185B")


def solar_data(df):
    st.markdown("### Solar Eclipse Insights")

    df["Eclipse Type Simple"] = df["Eclipse Type"].str[0].map({
        "A": "Annular",
        "H": "Hybrid",
        "P": "Partial",
        "T": "Total",
    })

    st.bar_chart(df["Eclipse Type Simple"].value_counts(), color="#E26F12")

    df["Hours"] = pd.to_datetime(df["Eclipse Time"], format="%H:%M:%S").dt.hour
    hour_eclipse = df["Hours"].value_counts().sort_index()

    st.markdown("### Eclipses Hourly")
    st.bar_chart(hour_eclipse, color="#E26F12")


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

    if DATASET == "solar":
        solar_data(df)
    if DATASET == "lunar":
        lunar_data(df)


if __name__ == "__main__":
    main()
