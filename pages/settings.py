import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import auth_functions
st.set_page_config(page_title="Settings",layout='wide')


col1,col2 = st.columns([1,20])

with col1:
        m = st.button('⬅️')
        if m:
            st.switch_page('pages/home.py')
      


with col2:
    st.header('User information:')
    try:
        st.write(st.session_state.user_info)
    except Exception:
        st.switch_page('app.py')

    # Sign out
    

    st.header('Sign out:')
    st.button(label='Sign Out',on_click=auth_functions.sign_out,type='primary')

    # Delete Account
    st.header('Delete account:')
    password = st.text_input(label='Confirm your password',type='password')
    st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')