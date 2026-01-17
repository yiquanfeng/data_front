import streamlit as st


pg = st.navigation([
    st.Page("csv_preview.py", title="CSV 预览", icon="📊"),
    st.Page("csv_upload.py", title="文件上传", icon="📁"),
    st.Page("show_file.py", title="文件预览", icon="📄"),
])

pg.run()