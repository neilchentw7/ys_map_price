import pandas as pd
import streamlit as st
import pydeck as pdk

st.set_page_config(page_title="混凝土報價地圖", layout="wide")

st.title("混凝土運送報價地圖")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

data = load_data("data/locations.csv")

# Show data table
with st.expander("查看所有地區資料"):
    st.dataframe(data)

# Map visualization
initial_view = pdk.ViewState(
    latitude=data["lat"].mean(),
    longitude=data["lon"].mean(),
    zoom=11,
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="[lon, lat]",
    get_color="[200, 30, 0, 160]",
    get_radius=200,
    pickable=True,
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=initial_view,
    tooltip={
        "text": "{name}\n單價: {price}\n坡度: {slope}\n可載米數: {capacity}",
    },
)

st.pydeck_chart(deck)
