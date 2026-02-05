import streamlit as st
import auth_functions



# Show user information
st.header('User information:')
try:
    st.write(st.session_state.user_info)
except Exception:
    st.switch_page('app.py')
    
st.balloons()
# Sign out
st.header('Sign out:')
st.button(label='Sign Out',on_click=auth_functions.sign_out,type='primary')

# Delete Account
st.header('Delete account:')
password = st.text_input(label='Confirm your password',type='password')
st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')