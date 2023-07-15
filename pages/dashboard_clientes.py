import streamlit as st

def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)
    pages = get_pages("app.py")

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )
        
    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")



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
        if st.button("Go Back"):
            switch_page("app")

with col2:
    with st.expander("Expanda-me"):
        st.success("Uhul Expandiu 2 baloes vindooo")
        st.balloons()