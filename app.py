import streamlit as st
import pydeck as pdk
import pandas as pd

st.title("Sample Map")

# Example data for a single point (San Francisco)
data = pd.DataFrame(
    {
        "lat": [37.7749],
        "lon": [-122.4194],
    }
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="[lon, lat]",
    get_color="[200, 30, 0, 160]",
    get_radius=200,
)

view_state = pdk.ViewState(
    latitude=data.loc[0, "lat"],
    longitude=data.loc[0, "lon"],
    zoom=10,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)

st.pydeck_chart(r)

