import streamlit as st

col1, col2 = st.columns([1, 2])

with col1:
    with st.expander():
        st.success("Uhul Expandiu")

with col2:
    with st.expander():
        st.success("Uhul Expandiu 2 baloes vindooo")
        st.balloons()