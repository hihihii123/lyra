import streamlit as st
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container
import random
import json
from backend import marco_invoke_qa_agent
import firestore_functions
from auth_functions import getUserId


try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')


def make_edits(id=0):
    try:
        part = st.session_state.study_thing[id]
    except Exception:
        st.switch_page('home.py')
        return False
    string = part
    while string[0] == "[":
        string =string[1:]
    while string[-1] == "]":
        string = string[:-1]
    inthing = string
    decoded = json.loads(inthing)
    
    #deepseek hepled me debug one of the bugs present
    if f'edit_data_{id}' not in st.session_state:
        st.session_state[f'edit_data_{id}'] = decoded.copy()
    
    working_data = st.session_state[f'edit_data_{id}']
    
    con = st.container(border=True,width="stretch")
    c = 0
    with con:
        for task in working_data['tasks']:
            name = task['name']
            new_name  = st.text_input(label="Name",value=name,key=f"name_{id}_{c}")
            due = task["duedate"]
            new_due = st.text_input(label="Due Date",value=due,key=f'due_{id}_{c}')
            complete = task['completionstatus']
            new_complete = st.text_input(label="Completion Status",value=complete,key=f'complete_{id}_{c}')
            complete_time = task['completiontime']
            new_complete_time = st.text_input(label="Completion Time",value=complete_time,key=f'time_{id}_{c}')
            
            working_data['tasks'][c]['name'] = new_name
            working_data['tasks'][c]['duedate'] = new_due
            working_data['tasks'][c]['completionstatus'] = new_complete
            working_data['tasks'][c]['completiontime'] = new_complete_time
        
            
            if st.button("Save what you have: ",key=f"button_{id}_{c}"):
                firebase_name = working_data['name']
                st.session_state.study_thing[id] = "[" + json.dumps(working_data) + "]"
                firestore_functions.writeorupdateDocument("users", getUserId(), {"data": st.session_state.study_thing[id]}, "studyplans", firebase_name)
                st.rerun()
            c += 1
        



#                 st.markdown(f"""
# <p class="pclass">Due Date: {task['duedate']}</p>
# """,unsafe_allow_html=True)

