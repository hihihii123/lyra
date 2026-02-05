import streamlit as st
import auth_functions



try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
    
st.balloons()




st.header("Welcome, user")

if st.button("Go to settings"):
    st.switch_page("./pages/settings.py")


