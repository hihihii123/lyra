import streamlit as st
import streamlit_extras
import time
from streamlit_extras.stylable_container import stylable_container
st.set_page_config(page_title="Onboarding",layout='wide')


try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')#Extracted through chatgpt
chapters = [
  "Computer Architecture",
  "Data Representation",
  "Logic Gates",
  "Programming",
  "Input Validation",
  "Testing and Debugging",
  "Algorithm Design",
  "Software Engineering",
  "Spreadsheets",
  "Networking",
  "Security and Privacy",
  "Intellectual Property",
  "Impact of Computing",
  "Emerging Technologies"
]
subtopics = {
  "Computer Architecture": [
    "Introduction to Computer Architecture",
    "Units of Data",
    "Components of a Computer System"
  ],

  "Data Representation": [
    "Introduction to Data Representation",
    "Understanding Number Systems and Conversion Techniques",
    "Representing Negative Numbers",
    "Representing Text"
  ],

  "Logic Gates": [
    "Boolean Logic",
    "Truth Tables",
    "Logic Gates",
    "Logic Circuits",
    "Manipulating Boolean Statements",
    "Solving System Problems"
  ],

  "Programming": [
    "Introduction to Algorithms and Programming",
    "Defining Problems",
    "Installing Python",
    "Comments",
    "Literals and Variables",
    "Functions, Methods and Operators",
    "Data Types",
    "Input and Output",
    "Booleans",
    "Integers and Floating-Point Numbers",
    "Strings",
    "Lists",
    "Dictionaries",
    "Control Flow",
    "User-Defined Functions",
    "with Statements"
  ],

  "Input Validation": [
    "Why Validation is Needed",
    "Recovering from Invalid Input",
    "Common Validation Checks"
  ],

  "Testing and Debugging": [
    "Bugs and Debugging",
    "Types of Program Errors",
    "Designing Test Cases",
    "Common Debugging Techniques"
  ],

  "Algorithm Design": [
    "Introduction to Algorithm Design",
    "Decomposition",
    "Generalisation",
    "Common Problems and Solutions"
  ],

  "Software Engineering": [
    "Stages in Developing a Program",
    "Alternative Methodologies"
  ],

  "Spreadsheets": [
    "Understanding Spreadsheets",
    "Logical Operators and Functions",
    "Mathematical and Statistical Operators and Functions",
    "Text Functions",
    "Lookup Functions",
    "Date Functions",
    "Goal Seek",
    "Conditional Formatting"
  ],

  "Networking": [
    "Introduction to Computer Networks",
    "Types of Computer Networks",
    "Protocols and Error Detection",
    "Home Networks and the Internet"
  ],

  "Security and Privacy": [
    "Defining Security and Privacy",
    "Threats",
    "Defences",
    "Analysis"
  ],

  "Intellectual Property": [
    "Introduction to Intellectual Property",
    "Copyright",
    "Software Licenses",
    "Software Piracy",
    "Copyright Infringement"
  ],

  "Impact of Computing": [
    "Impact of Computing on Different Industries",
    "Proliferation of Falsehoods"
  ],

  "Emerging Technologies": [
    "Artificial Intelligence",
    "Other Emerging Technologies"
  ]
}
task_obj_list = []




class study_task:
    """
    Access chapter and topics more easily
    """
    def __init__(self,x:int,y:int):
        self.x = x
        self.y=y
    def getitem(self):
        return [chapters[self.x],subtopics[chapters[self.x]][self.y]]
task_list = [study_task(0,0).getitem()]
if 'tasklist' not in st.session_state:
    st.session_state['tasklist'] = [study_task(0,0).getitem()]
else:
    task_list = st.session_state['tasklist']
st.markdown("""
<style>
.stApp{
            background-image: linear-gradient(to bottom,#CD63A9B3,#2A5B9B)
            }
</style>

""",unsafe_allow_html=True)

col1,col2,col3, = st.columns([1,17,1])
with col1:
    if st.button('⬅️'):
        st.switch_page('./pages/home.py')
with col2:
    con = st.container(width='stretch')
    with con:
        st.markdown("""
            <h1 style='color:white'r>
            Create Study Tasks
            </h1>
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
                    height:750px;
                    border-radius:25px;
                    justify-content:left;
                    padding:50px;
                    background:#e6e6e6;
                    }
                     """):
            print("WHATTT",task_list)
            for i in range(len(task_list)):
                task_obj_list.append(st.empty())
                task_obj_list[i] = st.container(border=True)
                with task_obj_list[i]:
                    sub1,sub2 = st.columns([15,1])
                    with sub1:
                        task_list[i][0] = st.selectbox("Chapter",chapters,index=chapters.index(task_list[i][0]),key=f'tasklist_0_{i}')
                        print('weirdlist',subtopics[task_list[i][0]])
                        if task_list[i][1] in subtopics:
                            task_list[i][1] = st.selectbox("Topic",subtopics[task_list[i][0]],index=subtopics[task_list[i][0]].index(task_list[i][1]),key=f'tasklist_1_{i}')
                        else:
                            task_list[i][1] = st.selectbox("Topic",subtopics[task_list[i][0]],key=f'tasklist_1_{i}')
                    with sub2:
                        if st.button('❌',key=f'task_delete_{i}'):
                            print('bad boy')

            if st.button('Add one more?'):
                task_list.append(study_task(chapters.index(task_list[-1][0]),subtopics[task_list[-1][0]].index(task_list[-1][1])).getitem())
                time.sleep(0.1)
            st.session_state['tasklist'] = task_list

            print(task_list,'NICE TASKLIST')


            

        #             <h1>
        #              &nbsp;&nbsp;&nbsp;Welcome To Lyra!
        #             </h1>
        #             <p>GET STARTED SETTING UP YOUR ACCOUNT</p>
        #             <div id="boxid">""",unsafe_allow_html=True)
        # button_container = st.container()

        # st.markdown("""
        #             </div>
        #             <style>
        #             @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
        #             @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
        #             h1{
        #             text-align:center;
        #             font-family: 'Comic';sans-serif;
        #             }
        #             p{
        #             text-align:center;
        #             font-family: 'Inter';sans-serif;
        #             }
        #             #boxid{
        #             flex:auto;
        #             height:500px;
        #             border:1px solid #0000ff;
        #             border-radius:25px;
        #             justify-content:center;
        #             padding:50px;
        #             background-color:white;
        #             }
        #             </style>
        #             """
        #             ,unsafe_allow_html=True)
        # with button_container:
        #     st.button('hi!')
        
        
