import streamlit as st
import pandas as pd
import io

st.title("اطلس مساجد")

# آپلود فایل اکسل
uploaded_file = st.file_uploader("فایل اکسل را انتخاب کنید", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.write("پیش نمایش داده‌ها:")
    st.dataframe(df)

    # تبدیل DataFrame به بایت‌ها برای دانلود
    def convert_df(df):
        output = io.BytesIO()
        df.to_excel(output, index=False)
        processed_data = output.getvalue()
        return processed_data

    # دکمه دانلود
    st.download_button(
        label="دانلود فایل اکسل اصلاح شده",
        data=convert_df(df),
        file_name='atlas_masajed.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
