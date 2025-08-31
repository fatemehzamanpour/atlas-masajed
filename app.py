import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

st.set_page_config(page_title="اطلس مساجد", layout="wide")
st.title("اطلس مساجد")

uploaded_file = st.file_uploader("فایل اکسل را آپلود کنید", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df['اشکالات'] = ""  # ستون اشکالات جدید اضافه می‌کنیم

    # هایلایت زرد و قرمز و سبز
    def highlight_row(row):
        color = ''
        if 'خطای تکراری' in row.get('اشکالات', ''):
            color = 'red'
        elif 'اصلاح شده' in row.get('اشکالات', ''):
            color = 'green'
        elif 'عدم تطابق' in row.get('اشکالات', ''):
            color = 'yellow'
        return ['background-color: {}'.format(color) for _ in row]

    # بررسی نام مسجد (نمونه)
    def check_name(name):
        if pd.isna(name) or name.strip() == "":
            return "نام مسجد ثبت نشده"
        return ""

    # نمونه بررسی روی ستون نام مسجد
    df['اشکالات'] = df['نام مسجد'].apply(lambda x: check_name(x))

    st.subheader("نتایج بررسی")
    st.dataframe(df.style.apply(highlight_row, axis=1))

    # امکان دانلود خروجی
    def convert_df(df):
        return df.to_excel(index=False)

    st.download_button(
        label="دانلود فایل بررسی شده",
        data=convert_df(df),
        file_name='output.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
