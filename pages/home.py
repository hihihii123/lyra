import streamlit as st
from auth_functions import getUserId
from streamlit_extras.stylable_container import stylable_container
from backend import invoke_qa_agent
from pages.temppage2 import make_nice_task,summary
st.set_page_config(page_title="Home",layout='wide')


try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
if not "balon" in st.session_state:
    st.balloons()
    st.session_state['balon'] = 'bleh'

recent_study_things = [] #to fill up
if "study_thing" in st.session_state:
     recent_study_things = st.session_state.study_thing



uid = getUserId()
st.header(f"Welcome, user: {uid}")
col1,col2,col3 = st.columns([3,6,1])
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
             st.text("There doesn't seem to be any recent study tasks!")
             if st.button("create one!"):
                  st.switch_page("./pages/study_page.py")
            
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
             
             st.write("okay you were studying thats good")
             from pages.temppage2 import summary
             for thing in recent_study_things:
                  summary(thing)
    if st.button('switch to temppage'):
         st.switch_page('./pages/temppage2.py')
with col2:
    #temp to test integration
    if st.button("Make a plan!"):
        st.switch_page("./pages/study_page.py")
    ohmydays = st.text_input("input smth ig")
    if ohmydays:
         oh = invoke_qa_agent(ohmydays)
         st.text(oh)
    
         

with col3:
        if st.button("⚙️"):
             st.switch_page("./pages/settings.py")


