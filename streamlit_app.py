import streamlit as st
import pandas as pd

st.title("Trang web hiển thị Google Sheets của tôi 🚀")

# Chuyển link Google Sheet sang dạng xuất file CSV
sheet_url = "LINK_CỦA_BẠN_Ở_ĐÂY"
csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

# Đọc dữ liệu
df = pd.read_csv(csv_url)

# Hiển thị lên web
st.write("Dữ liệu mới nhất:")
st.dataframe(df)

st.bar_chart(df.iloc[:, 1]) # Thử vẽ biểu đồ cột cho cột thứ 2
