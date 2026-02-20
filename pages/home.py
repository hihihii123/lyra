import streamlit as st
from auth_functions import getUserId
from streamlit_extras.stylable_container import stylable_container



try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
    
st.balloons()

recent_study_things = [] #to fill up



uid = getUserId()
st.header(f"Welcome, user: {uid}")
col1,col2,col3 = st.columns([4,6,1])
with col1:
    if len(recent_study_things)==0:
        with stylable_container(key="goback",css_styles="""
    {
                        flex:auto;
                        height:700px;
                        border-radius:25px;
                        justify-content:center;
                        padding:50px;
                        background-color:#91b5d9;
                        }
                        """):
             st.text("There doesn't seem to be any recent study things!")
             st.button("create one!")
    else:
        with stylable_container(key="goback",css_styles="""
            {
                                flex:auto;
                                height:700px;
                                border-radius:25px;
                                justify-content:left;
                                padding:50px;
                                background-color:#91b5d9;
                                }
                                """):
             st.write("okay you were studying thats goos")

with col3:
        if st.button("⚙️"):
             st.switch_page("./pages/settings.py")


