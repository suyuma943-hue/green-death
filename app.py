import streamlit as st
import streamlit.components.v1 as components

# Streamlitの余白を消して画面いっぱいに表示する設定
st.set_page_config(layout="wide")

# HTMLファイルを読み込む
with open("野生動物・分解データプラットフォーム.htm", "r", encoding="utf-8") as f:
    html_content = f.read()

# 高さと幅を広げてきれいに表示
components.html(html_content, height=1000, scrolling=True)
