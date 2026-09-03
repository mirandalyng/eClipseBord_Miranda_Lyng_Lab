import streamlit as st
import httpx
import pandas as pd
from pathlib import Path
import os

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

IMAGES_DIR = Path(
    os.getenv("IMAGES_DIR", Path(__file__).parents[3] / "images"))


def get_data(DATASET):
    response = httpx.get(f"{BASE_URL}/eclipse/{DATASET}", timeout=10)
    data = response.json()
    return pd.DataFrame(data)


def show_dataset(df):
    st.markdown("### Eclipse Data")
    st.dataframe(df)


def lunar_dict():

    words = st.selectbox(
        "Choose a type to learn more:", ["Total Lunar Eclipse", "Partial Lunar Eclipse", "Penumbral Eclipse"])

    if words == "Total Lunar Eclipse":
        st.info(
            "The Moon passes fully into Earth's umbra and turns reddish as only long-wavelength sunlight filters through Earth's atmosphere.")

    if words == "Partial Lunar Eclipse":
        st.info(
            "The Moon passes through only part of Earth's umbra, so the shadow grows and recedes without ever fully covering it.")

    if words == "Penumbral Eclipse":
        st.info(
            "The Moon passes through Earth's faint outer shadow, dimming so slightly it's easy to miss.")


def eclipse_type_lunar(df):
    st.caption("Shows how many lunar eclipses of each type have occurred.")

    df["Eclipse Type Simple"] = df["Eclipse Type"].str[0].map({
        "N": "Penumbral",
        "P": "Partial",
        "T": "Total",
    })

    st.bar_chart(df["Eclipse Type Simple"].value_counts(), color="#3F185B")


def hourly_lunar(df):
    st.markdown("### Eclipses Hourly")
    st.caption("Shows what time of day eclipses most commonly occur.")

    df["Hours"] = pd.to_datetime(df["Eclipse Time"], format="%H:%M:%S").dt.hour
    hour_eclipse = df["Hours"].value_counts().sort_index()

    st.bar_chart(hour_eclipse, color="#3F185B")


def lunar_data(df):
    st.markdown("### Lunar Eclipse Insights")
    lunar_dict()
    eclipse_type_lunar(df)
    hourly_lunar(df)


def solar_dict():

    words = st.selectbox(
        "Choose a type to learn more:", ["Total Solar Eclipse", "Annular Solar Eclipse", "Partial Solar Eclipse", "Hybrid Solar Eclipse", "Gamma", "Sun Altitude"])

    if words == "Total Solar Eclipse":
        st.info(
            "The Moon completely blocks the Sun, darkening the sky and revealing the Sun's corona.")

    if words == "Annular Solar Eclipse":
        st.info(
            "The Moon is too far from Earth to fully cover the Sun, leaving a bright ring visible around it.")

    if words == "Partial Solar Eclipse":
        st.info(
            "The Moon covers only part of the Sun, giving it a crescent shape.")

    if words == "Hybrid Solar Eclipse":
        st.info(
            "The eclipse shifts between total and annular as the Moon's shadow moves across the curved Earth.")

    if words == "Gamma":
        st.info(
            "Gamma measures how close the Moon's shadow passes to the center of the Earth; values near 0 mean a more central, direct eclipse.")

    if words == "Sun Altitude":
        st.info(
            "Sun Altitude is how high the Sun sits above the horizon at the moment of greatest eclipse.")


def eclipse_type_solar(df):
    st.markdown("### Eclipse Type")
    st.caption("Shows how many solar eclipses of each type have occurred.")
    # maps based on the first letter in the eclipse type
    df["Eclipse Type Simple"] = df["Eclipse Type"].str[0].map({
        "A": "Annular",
        "H": "Hybrid",
        "P": "Partial",
        "T": "Total",
    })

    # counts the amount and shows it in a barchart
    st.bar_chart(df["Eclipse Type Simple"].value_counts(), color="#E26F12")


def gamma_sun_alt(df):
    st.markdown("### Gamma vs Sun Altitude")
    st.caption("Gamma shows how close the Moon's shadow passes to Earth's center. "
               "Eclipses with extreme gamma values tend to occur when the Sun is lower in the sky.")
    st.scatter_chart(df, x="Gamma", y="Sun Altitude",
                     color="Eclipse Type Simple")


def hourly_eclipse(df):
    st.markdown("### Eclipses Hourly")
    st.caption("Shows what time of day eclipses most commonly occur.")
    # converts to a real timestamp and takes the hour to be able to show how many hourly eclipses there is
    df["Hours"] = pd.to_datetime(df["Eclipse Time"], format="%H:%M:%S").dt.hour
    hour_eclipse = df["Hours"].value_counts().sort_index()

    st.bar_chart(hour_eclipse, color="#E26F12")


def gamma_magnitude(df):
    st.markdown("### Gamma vs Magnitude")
    st.caption("Magnitude shows how much of the Sun is covered. Eclipses closer to the center "
               "(low |Gamma|) reach near-total coverage, while off-center eclipses (high |Gamma|) "
               "are only partial.")
    df["Abs Gamma"] = df["Gamma"].abs()
    st.scatter_chart(df, x="Abs Gamma", y="Eclipse Magnitude",
                     color="Eclipse Type Simple")


def solar_data(df):
    st.markdown("### Solar Eclipse Insights")

    solar_dict()

    eclipse_type_solar(df)

    gamma_sun_alt(df)

    hourly_eclipse(df)

    gamma_magnitude(df)


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
