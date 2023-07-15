import streamlit as st
import pandas as pd
import sqlite3
# from streamlit_extras.switch_page_button import switch_page

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


st.image("src/imgs/logo.png")
st.header("DataFusion")

# st.markdown("---", unsafe_allow_html = True)

con = sqlite3.connect("data/data.db")
cur = con.cursor()
can_pass = False

tab_login, tab_create = st.tabs(["Login", "Create your account"])


if tab_login:
    with tab_login:
        placeholder_login = st.empty()
        with placeholder_login.form("login"):
            email = st.text_input("Email")
            password = st.text_input("Password", type = "password")
            submit = st.form_submit_button("Login")

        if submit and email:
            data = pd.read_sql_query("SELECT * from usuarios", con)

            for _, col in data.iterrows():
                if email == str(col.email) and password == str(col.password):
                    auth = True
                    break
                else:
                    auth = False
                    continue

            if "auth" in globals():
                if auth != False:
                    can_pass = True
                    placeholder_login.empty()
                    st.success("Login authenticated!")
                else:
                    st.error("User not authenticated")
            else:
                pass

        elif submit and not email:
            st.warning("Please put your email")

if tab_create:
    with tab_create:
        placeholder_create = st.empty()
        with placeholder_create.form("create"):
            email_create = st.text_input("Email")
            password_create = st.text_input("Password", type = "password")
            confirm_password = st.text_input("Confirm your password", type = "password")
            send = st.form_submit_button("Create Account")

            if send:
                if not email_create:
                    st.warning("Please input your email.")
                elif not password_create:
                    st.warning("Please input your password.")
                elif not confirm_password:
                    st.warning("Please input the confirm password.")
                elif password_create != confirm_password:
                    st.warning("Password doesn't match to confirm password")
                else:
                    cur.execute(f"INSERT INTO usuarios (email,password) VALUES (?,?);", (email_create, password_create)).fetchall()
                    con.commit()                
                    st.success("Login created successfully!!!")

if "data" in globals():
    
    st.dataframe(data)

if can_pass != False:
    switch_page("dashboard_clientes")


con.close()
