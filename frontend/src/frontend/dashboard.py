import streamlit as st
import httpx


BASE_URL = "http: // 127.0.0.1: 8000/eclipse/"


def main():
    st.markdown("# Eclipse data")

    stats = httpx.get
