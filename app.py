import streamlit as st
import auth_functions
from PIL import Image
from streamlit_extras.stylable_container import stylable_container
im = Image.open('favicon.jpeg')
newuser = False

# Background colour + title
st.set_page_config(page_title="Lyra", page_icon=im,layout="wide")
st.markdown("""
<style>
.stApp{
            background-image: linear-gradient(to bottom,#CD63A9B3,#2A5B9B)
            }
</style>

""",unsafe_allow_html=True)


## NOT LOGGED IN
#adapted from some streamlit help
col1,col2,col3, = st.columns([7,2,2])

with col1:
    con = st.container()
    with con:
        st.markdown("""
            <h1 style='color:white'r>
                Lyra!
            </h1>
            <p id='id1'>Your Computing Study Buddy</p>
            <style>
                                        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
                    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
                    h1{
                    text-align:left;
                    font-family: 'Comic', sans-serif;
                    }
                    #id2{
                    color: white;
                    }
                    p{
                    text-align:left;
                    font-family: 'Inter', sans-serif;
                    }
                    #id1{
                    color: white;
                    }
            </style>
            """,unsafe_allow_html=True)
        with stylable_container(key="goback",css_styles="""
{
                    flex:auto;
                    height:450px;
                    border-radius:25px;
                    justify-content:left;
                    padding:50px;
                    background:#e6e6e6;
                    }
                     """):
            if 'user_info' not in st.session_state:
                col2,col1 = st.columns([7,1])

                # Authentication form layout
                do_you_have_an_account = col2.selectbox(label='Do you have an account?',options=('Yes','No','I forgot my password'),width=200)
                auth_form = col2.form(key='Authentication form',clear_on_submit=False,width='stretch')
                email = auth_form.text_input(label='Email')
                password = auth_form.text_input(label='Password',type='password') if do_you_have_an_account in {'Yes','No'} else auth_form.empty()
                auth_notification = col2.empty()

                # Sign In
                if do_you_have_an_account == 'Yes' and auth_form.form_submit_button(label='Sign In',use_container_width=True,type='primary'):
                    with auth_notification, st.spinner('Signing in'):
                        auth_functions.sign_in(email,password)

                # Create Account
                elif do_you_have_an_account == 'No' and auth_form.form_submit_button(label='Create Account',use_container_width=True,type='primary'):
                    with auth_notification, st.spinner('Creating account'):
                        auth_functions.create_account(email,password)
                    newuser = True

                # Password Reset
                elif do_you_have_an_account == 'I forgot my password' and auth_form.form_submit_button(label='Send Password Reset Email',use_container_width=True,type='primary'):
                    with auth_notification, st.spinner('Sending password reset link'):
                        auth_functions.reset_password(email)

                # Authentication success and warning messages
                if 'auth_success' in st.session_state:
                    auth_notification.success(st.session_state.auth_success)
                    del st.session_state.auth_success
                elif 'auth_warning' in st.session_state:
                    auth_notification.warning(st.session_state.auth_warning)
                    del st.session_state.auth_warning

## LOGGED IN
            else:
                # Switches pages 
                if newuser:
                    st.switch_page("./pages/onboarding.py")
                else:
                    st.switch_page("./pages/home.py")
            

# if 'user_info' not in st.session_state:
#     col2,col1,col3 = st.columns([3,2,1])

#     # Authentication form layout
    
#     do_you_have_an_account = col2.selectbox(label='Do you have an account?',options=('Yes','No','I forgot my password'))
#     auth_form = col2.form(key='Authentication form',clear_on_submit=False)
#     email = auth_form.text_input(label='Email')
#     password = auth_form.text_input(label='Password',type='password') if do_you_have_an_account in {'Yes','No'} else auth_form.empty()
#     auth_notification = col2.empty()

#     # Sign In
#     if do_you_have_an_account == 'Yes' and auth_form.form_submit_button(label='Sign In',use_container_width=True,type='primary'):
#         with auth_notification, st.spinner('Signing in'):
#             auth_functions.sign_in(email,password)

#     # Create Account
#     elif do_you_have_an_account == 'No' and auth_form.form_submit_button(label='Create Account',use_container_width=True,type='primary'):
#         with auth_notification, st.spinner('Creating account'):
#             auth_functions.create_account(email,password)
#         newuser = True

#     # Password Reset
#     elif do_you_have_an_account == 'I forgot my password' and auth_form.form_submit_button(label='Send Password Reset Email',use_container_width=True,type='primary'):
#         with auth_notification, st.spinner('Sending password reset link'):
#             auth_functions.reset_password(email)

#     # Authentication success and warning messages
#     if 'auth_success' in st.session_state:
#         auth_notification.success(st.session_state.auth_success)
#         del st.session_state.auth_success
#     elif 'auth_warning' in st.session_state:
#         auth_notification.warning(st.session_state.auth_warning)
#         del st.session_state.auth_warning

# ## -------------------------------------------------------------------------------------------------
# ## Logged in --------------------------------------------------------------------------------------
# ## -------------------------------------------------------------------------------------------------
# else:
#     if newuser:
#         st.switch_page("./pages/onboarding.py")
#     else:
#         st.switch_page("./pages/home.py")
    # # Show user information
    # st.header('User information:')
    # st.write(st.session_state.user_info)
    # st.balloons()
    # # Sign out
    # st.header('Sign out:')
    # st.button(label='Sign Out',on_click=auth_functions.sign_out,type='primary')

    # # Delete Account
    # st.header('Delete account:')
    # password = st.text_input(label='Confirm your password',type='password')
    # st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')
if st.button('[DEBUG] check onboarding'):
    st.switch_page("./pages/onboarding.py")