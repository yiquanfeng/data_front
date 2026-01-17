import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="军事文件预览")

def load_data(csv_file):
    # 使用 skipinitialspace=True 自动处理逗号后的空格
    data = pd.read_csv(csv_file, skipinitialspace=True)
    # 进一步确保列名没有两端空格
    data.columns = data.columns.str.strip()

    return data

def better_display(data, url_render_column):
    return st.data_editor(
        data,
        column_config={
            url_render_column: st.column_config.LinkColumn(
                help="点击下载文件",
                display_text="下载链接",
                width="medium",
            ),
            "distract": st.column_config.TextColumn(width="medium"),
        },
        height=800,
        hide_index=True,
        use_container_width=True
    )


st.title("军事文件信息预览")
data = load_data('example.csv')
data_render = better_display(data, 'file_url')