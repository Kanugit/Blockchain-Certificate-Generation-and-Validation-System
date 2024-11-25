import streamlit as st
from db.firebase_app import login
from dotenv import load_dotenv
import os
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

# Streamlit page setup
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

load_dotenv()

form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")

if st.session_state.profile != "Institute":
    clicked_register = st.button("New user? Click here to register!")
    if clicked_register:
        switch_page("register")

submit = form.form_submit_button("Login")
if submit:
    result = login(email, password)
    if result == "success":
        st.success("Login successful!")
        # Redirect based on profile
        if st.session_state.profile == "Institute":
            switch_page("institute")  # Direct to Institute dashboard
        else:
            switch_page("verifier")  # Direct to Verifier dashboard
    else:
        st.error("Invalid credentials!")
