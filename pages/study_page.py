import streamlit as st
import streamlit_extras
import time
from streamlit_extras.stylable_container import stylable_container
st.set_page_config(page_title="Onboarding",layout='wide')
from backend import invoke_qa_agent
class task:
    chapter: int
    topic: int
    confidence: int

try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
#Extracted through chatgpt
chapters = [
  "1. Computer Architecture",
  "2. Data Representation",
  "3. Logic Gates",
  "4. Programming",
  "5. Input Validation",
  "6. Testing and Debugging",
  "7. Algorithm Design",
  "8. Software Engineering",
  "9. Spreadsheets",
  "10. Networking",
  "11. Security and Privacy",
  "12. Intellectual Property",
  "13. Impact of Computing",
  "14. Emerging Technologies"
]
subtopics = {
  "1. Computer Architecture": [
    "1.1 Introduction to Computer Architecture",
    "1.2 Units of Data",
    "1.3 Components of a Computer System",
    "Entire Chapter"
  ],

  "2. Data Representation": [
    "2.1 Introduction to Data Representation",
    "2.2 Understanding Number Systems and Conversion Techniques",
    "2.3 Representing Negative Numbers",
    "2.4 Representing Text",
    "Entire Chapter"


  ],

  "3. Logic Gates": [
    "3.1 Boolean Logic",
    "3.2 Truth Tables",
    "3.3 Logic Gates",
    "3.4 Logic Circuits",
    "3.5 Manipulating Boolean Statements",
    "3.6 Solving System Problems",
    "Entire Chapter"
  ],

  "4. Programming": [
    "4.1 Introduction to Algorithms and Programming",
    "4.2 Defining Problems",
    "4.3 Installing Python",
    "4.4 Comments",
    "4.5Literals and Variables",
    "4.6 Functions, Methods and Operators",
    "4.7 Data Types",
    "4.8 Input and Output",
    "4.9 Booleans",
    "4.10 Integers and Floating-Point Numbers",
    "4.11 Strings",
    "4.12 Lists",
    "4.13 Dictionaries",
    "4.14 Control Flow",
    "4.15 User-Defined Functions",
    "4.16 with Statements",
    "Entire Chapter"
  ],

  "5. Input Validation": [
    "5.1 Why Validation is Needed",
    "5.2 Recovering from Invalid Input",
    "5.3 Common Validation Checks",
    "5.4 Entire Chapter"
  ],

  "6. Testing and Debugging": [
    "6.1 Bugs and Debugging",
    "6.2 Types of Program Errors",
    "6.3 Designing Test Cases",
    "6.4 Common Debugging Techniques",
    "Entire Chapter"
  ],

  "7. Algorithm Design": [
    "7.1 Introduction to Algorithm Design",
    "7.2 Decomposition",
    "7.3 Generalisation",
    "7.4 Common Problems and Solutions",
    "Entire Chapter"
  ],

  "8. Software Engineering": [
    "8.1 Stages in Developing a Program",
    "8.2 Alternative Methodologies",
    "Entire Chapter"
  ],

  "9. Spreadsheets": [
    "9.1 Understanding Spreadsheets",
    "9.2 Logical Operators and Functions",
    "9.3 Mathematical and Statistical Operators and Functions",
    "9.4 Text Functions",
    "9.5 Lookup Functions",
    "9.6 Date Functions",
    "9.7 Goal Seek",
    "9.8 Conditional Formatting",
    "Entire Chapter"
  ],

  "10. Networking": [
    "10.1 Introduction to Computer Networks",
    "10.2 Types of Computer Networks",
    "10.3 Protocols and Error Detection",
    "10.4 Home Networks and the Internet",
    "Entire Chapter"
  ],

  "11. Security and Privacy": [
    "11.1 Defining Security and Privacy",
    "11.2Threats",
    "11.3 Defences",
    "11.4 Analysis",
    "Entire Chapter"
  ],

  "12. Intellectual Property": [
    "12.1 Introduction to Intellectual Property",
    "12.2 Copyright",
    "12.3 Software Licenses",
    "12.4 Software Piracy",
    "12.5 Copyright Infringement",
    "12.6 Entire Chapter"
  ],

  "13. Impact of Computing": [
    "13.1 Impact of Computing on Different Industries",
    "13.2 Proliferation of Falsehoods",
    "Entire Chapter"
  ],

  "14. Emerging Technologies": [
    "14.1 Artificial Intelligence",
    "14.2 Other Emerging Technologies",
    "Entire Chapter"
  ]
}
task_obj_list = []
#matthias look here
@st.dialog("Create study plan?",dismissible=False)
def submit_plan():
    st.write("Do you want to create study plan?")
    _,col1,col2,_ = st.columns([2,1,1,2])
    with col1:
      if st.button("Yes!"):
          st.write(invoke_qa_agent(task_list))
    with col2:
      if st.button("No"):
          st.rerun()



class study_task:
    """
    Access chapter and topics more easily
    Parameters:
    z: user confidence in subtopic
    """
    def __init__(self,x:int,y:int,z:int,comments:str):
        self.x = x
        self.y=y
        self.z = z
        self.comments = comments
    def getitem(self):
        return [chapters[self.x],subtopics[chapters[self.x]][self.y],self.z,self.comments]
task_list = [study_task(0,0,5,'').getitem()]
if 'tasklist' not in st.session_state:
    print('activate first')
    st.session_state['tasklist'] = [study_task(0,0,5,'').getitem()]
else:
    print('activate second')
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
                    height:auto;
                    border-radius:25px;
                    justify-content:left;
                    padding:50px;
                    background:#e6e6e6;
                    }
                     """):
            temp = []
            changed = False
            for i in range(len(task_list)):
                if task_list[i][0] != None:
                    temp.append([task_list[i][0],task_list[i][1],task_list[i][2],task_list[i][3]]) #Matthias you can optimize this
            task_list = temp
            for i in range(len(task_list)):
                task_obj_list.append(st.empty())
                task_obj_list[i] = st.container(border=True)
                with task_obj_list[i]:
                    sub1,sub2 = st.columns([15,1])
                    with sub1:
                        task_list[i][0] = st.selectbox("Chapter",chapters,index=chapters.index(task_list[i][0]),key=f'tasklist_0_{i}')
                        #print('weirdlist',subtopics[task_list[i][0]])
                        #print('values',sum(subtopics.values(),[]))
                        if task_list[i][1] in subtopics[task_list[i][0]]:
                            task_list[i][1] = st.selectbox("Topic",subtopics[task_list[i][0]],index=subtopics[task_list[i][0]].index(task_list[i][1]),key=f'tasklist_1_{i}')
                        else:
                            task_list[i][1] = st.selectbox("Topic",subtopics[task_list[i][0]],key=f'tasklist_1_{i}')
                        task_list[i][2] = st.slider("How confident are you in the topic?",0,10,5,key=f'tasklist_2_{i}')
                        task_list[i][3] = st.text_area("Other comments",key=f"tasklist_3_{i}")
                    with sub2:
                        if st.button('❌',key=f'task_delete_{i}'):
                            #print("Lenght of things",task_list)
                            #print("I",i)
                            task_list[i][0] = task_list[i][1] = None
                            changed=True
            if changed:
                st.session_state['tasklist'] = task_list
                st.rerun()

            st.session_state['tasklist'] = task_list
            if st.button('Add task'):
                if len(task_list) == 0:
                    task_list = [study_task(0,0,5,'').getitem()]
                else:
                    #print('THIS SHOULD NOT HAPPEN')
                    task_list.append(study_task(chapters.index(task_list[-1][0]),subtopics[task_list[-1][0]].index(task_list[-1][1]),5,'').getitem())
                st.session_state['tasklist'] = task_list
                st.rerun()
            if st.button("Create study plan!"):
                submit_plan()
                
                
          


            #print("WHATTT",task_list)

            

            #print(task_list,'NICE TASKLIST')


            

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
        
        
