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
                                height:auto;
                                border-radius:25px;
                                justify-content:left;
                                padding:50px;
                                background-color:#91b5d9;
                                }
                                """):
             
             st.write("okay you were studying thats good")
             from pages.temppage2 import summary
             c = 1
             for thing in recent_study_things:
                  if c > 3:
                       break
                  summary(thing,f"button_id_{c}")
                  c+= 1 #so that it wont be too crowded
    if st.button('switch to temppage'):
         st.switch_page('./pages/temppage2.py')
sample_str = '[{"name":"1. Computer Architecture - 1.1 Introduction to Computer Architecture and 1.2 Units of Data","description":"Study plan covering two subtopics within Chapter 1: Introduction to Computer Architecture and Units of Data.","tasks":[{"name":"1. Computer Architecture - 1.1 Introduction to Computer Architecture","confidencelevel":5,"chapter":1,"topic":1,"duedate":"2026-03-10","description":"Learn the fundamentals of computer architecture and its components; understand the interaction between CPU, memory and I/O; grasp the fetch-decode-execute cycle at a high level.","startdate":"2026-02-22","completionstatus":false,"completiontime":"","definitions":["Computer Architecture","CPU","ALU","Control Unit","Memory","Cache","Bus","ISA","Fetch-Decode-Execute cycle"],"guiding_qns":["What is computer architecture and how does it differ from computer organization?","Identify the main components of a CPU and their roles.","Explain the fetch-decode-execute cycle at a high level.","How do memory hierarchy and I/O devices interact with the CPU?","What factors influence overall system performance beyond CPU speed?"],"objectives":["Define Computer Architecture and describe its primary components.","Describe the role of CPU, memory, and I/O in a computer system and how they interact.","Outline the fetch-decode-execute cycle and why it is central to how computers operate.","Explain the basic memory hierarchy (registers, cache, RAM) and data flow between components."]},{"name":"1. Computer Architecture - 1.2 Units of Data","confidencelevel":5,"chapter":1,"topic":2,"duedate":"2026-03-10","description":"Explore units of data and how data size is measured, including bits, bytes, and larger units; learn conversion between units.","startdate":"2026-02-22","completionstatus":false,"completiontime":"","definitions":["bit","byte","nibble","word","kilobyte","megabyte","gigabyte","terabyte","binary prefix","decimal prefix"],"guiding_qns":["How many bits are in a byte, and what are common data size units?","How do you convert between bits and bytes, and between bytes and larger units (KB, MB, GB)?","What are the differences between binary prefixes (KiB, MiB) and decimal prefixes (KB, MB)?","Why do data size units matter for memory, storage, and data transfer?"],"objectives":["Define common data size units and their relationships (bit, byte, KB, MB, GB, TB).","Convert between data size units (bits ⇄ bytes; bytes ⇄ kilobytes, megabytes, gigabytes).","Explain practical implications of data sizes for memory capacity and data transfer rates."]}],"completionstatus":false,"comments":""}]'
with col2:
    #temp to test integration
    if st.button("Make a plan!"):
        st.switch_page("./pages/study_page.py")
    if st.button('add random plan for debug'):
         recent_study_things.append(sample_str)
         st.session_state.study_thing = recent_study_things

    # ohmydays = st.text_input("input smth ig")
    # if ohmydays:
    #      oh = invoke_qa_agent(ohmydays)
    #      st.text(oh)
    
         

with col3:
        if st.button("⚙️"):
             st.switch_page("./pages/settings.py")


