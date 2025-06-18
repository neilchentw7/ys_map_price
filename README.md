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

程式會讀取 `data/locations.csv` 中的資料，並在地圖上以標記方式呈現各地區的單價與其他提示資訊。
