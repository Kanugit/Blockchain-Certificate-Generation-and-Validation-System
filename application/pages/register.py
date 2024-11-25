import streamlit as st
from db.firebase_app import register
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

# Streamlit page setup
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

# Initialize 'profile' in session state if it doesn't exist
if "profile" not in st.session_state:
    st.session_state["profile"] = ""  # Default value

# Registration form
form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")

# Add a profile type selection
profile_type = form.selectbox("Select your profile type", ("Institute", "Verifier"))

submit = form.form_submit_button("Register")

# Login button outside the form if it’s for navigation
clicked_login = st.button("Already registered? Click here to login!")
if clicked_login:
    switch_page("login")

# Handle registration submission
if submit:
    result = register(email, password)
    if result == "success":
        st.success("Registration successful!")
        st.session_state.profile = profile_type  # Set the profile type in session state
        # Redirect based on profile
        if st.session_state.profile == "Institute":
            switch_page("login")  # Direct to Institute login page
        else:
            switch_page("verifier")  # Direct to Verifier page
    else:
        st.error("Registration unsuccessful!")
