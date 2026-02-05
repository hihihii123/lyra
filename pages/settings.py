import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import auth_functions


col1,col2 = st.columns([1,20])

with col1:
    with stylable_container(key="goback",css_styles="""
button {
                            background-color: Tomato;
                            }
button:hover {
                            background-color: green;
                            }
                     """):
        m = st.button('go back')
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