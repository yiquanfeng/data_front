import streamlit as st
import pandas as pd
import numpy as np

# 1. 设置页面配置为宽屏模式（这是实现全屏效果的第一步）
st.set_page_config(layout="wide", page_title="军事文件预览")

def load_data(csv_file):
    # 使用 skipinitialspace=True 自动处理逗号后的空格
    data = pd.read_csv(csv_file, skipinitialspace=True)
    # 进一步确保列名没有两端空格
    data.columns = data.columns.str.strip()
    # 确保 URL 数据本身也没有空格
    if 'file_url' in data.columns:
        data['file_url'] = data['file_url'].str.strip()
    return data

def render_url(data, column_name):
    # st.data_editor 本身就会在页面上显示表格
    return st.data_editor(
        data,
        column_config={
            column_name: st.column_config.LinkColumn(
                help="点击下载文件",
                display_text="下载链接",
                width="medium",  # 你可以设置为 "small", "medium", "large" 或像素值数字
            ),
            # 如果想控制其他列宽度，可以继续添加
            "distract": st.column_config.TextColumn(width="medium"),
        },
        height=800, # 2. 将高度设置为较大的值（例如 800-1000 像素），使其占据大部分屏幕
        hide_index=True,
        use_container_width=True # 3. 确保占满容器宽度
    )


st.title("军事文件信息预览")
data = load_data('example.csv')
# 直接调用即可，不需要再 st.write(data_render)
data_render = render_url(data, 'file_url')