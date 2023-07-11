import streamlit as st


st.set_page_config(initial_sidebar_state = "collapsed",
                   page_icon = "src/imgs/logo.png",
                   page_title = "DataFusion")

st.markdown(
    """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """,
    unsafe_allow_html = True)


col1, col2 = st.columns([1, 2])

with col1:
    with st.expander("Expanda-me"):
        st.success("Uhul Expandiu")

with col2:
    with st.expander("Expanda-me"):
        st.success("Uhul Expandiu 2 baloes vindooo")
        st.balloons()