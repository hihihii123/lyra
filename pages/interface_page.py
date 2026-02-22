import streamlit as st
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container
import random
import json
from backend import marco_invoke_qa_agent
from pages.temppage2 import make_nice_task
import firestore_functions
from auth_functions import getUserId

st.set_page_config(page_title="Interface",layout='wide')
try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
    

# Background colour
st.markdown("""
<style>
.stApp{
            background-image: linear-gradient(to bottom,#CD63A9B3,#2A5B9B)
            }
</style>

""",unsafe_allow_html=True)


col1,col2,col3, = st.columns([2,10,2])
with col1:
    if st.button('⬅️'):
        st.switch_page('./pages/study_page.py')
with col2:
    con = st.container(width='stretch')
    with con:
        st.markdown("""

            <style>
                                        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
                    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
                    h1{
                    text-align:center;
                    font-family: 'Comic';sans-serif;
                    }
                    #id2{
                    color: white;
                    }
                    p{
                    text-align:center;
                    font-family: 'Inter';sans-serif;
                    }
                    #id1{
                    color: white;
                    }
            </style>
            """,unsafe_allow_html=True)
        with stylable_container(key="goback",css_styles=""" 
{
                    flex:auto;
                    height:auto;
                    border-radius:25px;
                    justify-content:left;
                    padding:50px;
                    background:#e6e6e6;
                    }
                     """):
            if st.button("Send prompt"):
                #adapted from https://discuss.streamlit.io/t/how-to-show-local-gif-image/3408
                gif = st.empty()
                txt = st.empty()
                txt.write("Loading... Here's a GIF while waiting")
                selected = random.choice(['https://media.tenor.com/tpw97n05O70AAAAi/vacameme129.gif','https://media1.tenor.com/m/byY2-DioMQ4AAAAd/quirky-clown-bread-join-voice-call-vc.gif','https://media1.tenor.com/m/lfDATg4Bhc0AAAAC/happy-cat.gif','https://media1.tenor.com/m/fitGu2TwtHoAAAAd/cat-hyppy.gif'])
                gif.markdown(f"![GIF not playing :()]({selected})")
                string = marco_invoke_qa_agent(st.session_state['tasklist'],old_tasks="No old tasks")
                st.write(string)
                gif.empty()
                txt.empty()
                make_nice_task(string) 
                if "study_thing" not in st.session_state:
                    st.session_state.study_thing = []
                st.session_state.study_thing.append(string)
            

                newstring = json.loads(string)[0]
                name = newstring['name']
                firestore_functions.writeorupdateDocument("users", getUserId(), {"data": string}, "studyplans", name)