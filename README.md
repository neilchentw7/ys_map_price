# 混凝土運送報價地圖

這個專案示範如何使用 Streamlit 與 Google 地圖資料來快速查詢各地區混凝土報價以及坡度與載運量資訊。

## 安裝方式

```bash
pip install streamlit pandas pydeck
```

## 執行方式

```bash
streamlit run app.py
```

程式會讀取 `data/locations.csv` 中的資料，每筆資料包含 8 米到 1 米的分級單價、坡度、可載運米數、備註說明，以及該地的經緯度座標。地圖使用衛星底圖，並以標記方式呈現各地區資訊。您可以修改此 CSV 以新增或調整地區資訊。
