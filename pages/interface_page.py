import streamlit as st
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container
from backend import marco_invoke_qa_agent
st.set_page_config(page_title="Onboarding",layout='wide')

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
                string = marco_invoke_qa_agent(st.session_state['tasklist'],old_tasks="No old tasks")
                st.write(string)
            st.text('')
