import streamlit as st
import pandas as pd

def file_upload(dist_path):
    uploaded_file = st.file_uploader("上传CSV文件", type=["csv"])
    if not uploaded_file:
        st.info("请上传一个CSV文件以继续。")
        return pd.DataFrame()  # 返回空的DataFrame以防止后续错误
    data = pd.read_csv(uploaded_file, skipinitialspace=True)
    st.success("文件上传成功！")
    return data

st.title("筛选后的文件上传")
dist_path = 'filtered_files.csv'
data = file_upload(dist_path)
with open(dist_path, 'w', encoding='utf-8') as f:
    data.to_csv(f, index=False)