@echo off
streamlit.exe run ./app.py

with st.sidebar:
    st.markdown("## **Repository'miz**:")
    st.markdown("Kaynak kodu ve daha fazla bilgi için Repositroy'mize bakabilirsiniz")
    st.link_button("https://github.com/yazotech142")
    st.markdown("## **Biz Kimiz**")
    st.markdown(".")