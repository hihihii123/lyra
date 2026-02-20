import streamlit as st
from auth_functions import getUserId
from streamlit_extras.stylable_container import stylable_container
import json
strin1 = '[{ "name": "5. Input Validation (Chapter 5) - 5.3 Common Validation Checks", "description": "Study plan for understanding common validation checks used in input validation. This task covers presence, type, range, format, and boundary checks, with a focus on designing robust validation logic, handling invalid input, and preventing common security issues.", "tasks": [ { "name": "5. Input Validation - 5.3 Common Validation Checks", "confidencelevel": 5, "chapter": 5, "topic": 3, "duedate": "2026-02-27", "description": "Explore and implement common validation checks. Guiding questions and textbook-based objectives accompany this subtopic. Focus on designing checks and applying them to sample input scenarios.", "startdate": "2026-02-20", "completionstatus": false, "completiontime": "", "definitions": ["presence check", "type check", "range check", "length check", "format validation", "regex validation", "sanitization", "whitelist/blacklist validation", "boundary check", "consistency check"], "guiding_qns": [ "What is input validation and why is it important for software reliability and security?", "What different types of validation checks are commonly used (presence, type, range, length, format)?", "How do you implement each check for typical data types (numbers, strings, dates)?", "How should invalid input be handled and reported to the user?", "What are common regex patterns or formats used for validation in real-world applications?", "How does validation relate to sanitization and normalization of inputs?", "How would you test edge cases and boundary values for inputs?" ], "objectives": [ "Explain the purpose of input validation and identify common validation checks.", "Apply presence, type, range, length, and format checks to user inputs.", "Create validation logic for numeric, string, and date inputs.", "Provide meaningful feedback and error handling for invalid inputs.", "Recognize and mitigate security risks related to input handling (e.g., injection).", "Prepare unit tests to verify validation logic across edge cases." ] } ], "completionstatus": false, "comments": "New task from user input: 5. Input Validation - 5.3 Common Validation Checks." }]'

if st.button('⬅️',key='temppageback'):
    st.switch_page("./pages/home.py")
def make_nice_task(string):
    string = string[1:-1]
    decoded = json.loads(string)
    st.write(decoded)
    con = st.container(border=True,width=700)
    with con:
        h,sh = decoded['name'].split('-')
        st.header(h)
        st.subheader(sh)
        st.write(decoded['description'])
        for task in decoded['tasks']:
            with st.expander(task['name']):
                st.write(task['description'])
                st.write(f"Due date: {task['duedate']}")

    

if __name__ == "__main__":
    make_nice_task(strin1)
