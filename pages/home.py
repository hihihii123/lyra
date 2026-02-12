import streamlit as st
from auth_functions import getUserId



try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
    
st.balloons()



uid = getUserId()
st.header(f"Welcome, user: {uid}")

if st.button("Go to settings"):
    st.switch_page("./pages/settings.py")


