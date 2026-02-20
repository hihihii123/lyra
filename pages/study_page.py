import streamlit as st
import streamlit_extras
import time
from streamlit_extras.stylable_container import stylable_container
st.set_page_config(page_title="Onboarding",layout='wide')


try:
    var = st.session_state.user_info
except Exception:
    st.switch_page('app.py')
#Extracted through chatgpt
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
    "Components of a Computer System",
    "Entire Chapter"
  ],

  "Data Representation": [
    "Introduction to Data Representation",
    "Understanding Number Systems and Conversion Techniques",
    "Representing Negative Numbers",
    "Representing Text",
    "Entire Chapter"


  ],

  "Logic Gates": [
    "Boolean Logic",
    "Truth Tables",
    "Logic Gates",
    "Logic Circuits",
    "Manipulating Boolean Statements",
    "Solving System Problems",
    "Entire Chapter"
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
    "with Statements",
    "Entire Chapter"
  ],

  "Input Validation": [
    "Why Validation is Needed",
    "Recovering from Invalid Input",
    "Common Validation Checks",
    "Entire Chapter"
  ],

  "Testing and Debugging": [
    "Bugs and Debugging",
    "Types of Program Errors",
    "Designing Test Cases",
    "Common Debugging Techniques",
    "Entire Chapter"
  ],

  "Algorithm Design": [
    "Introduction to Algorithm Design",
    "Decomposition",
    "Generalisation",
    "Common Problems and Solutions",
    "Entire Chapter"
  ],

  "Software Engineering": [
    "Stages in Developing a Program",
    "Alternative Methodologies",
    "Entire Chapter"
  ],

  "Spreadsheets": [
    "Understanding Spreadsheets",
    "Logical Operators and Functions",
    "Mathematical and Statistical Operators and Functions",
    "Text Functions",
    "Lookup Functions",
    "Date Functions",
    "Goal Seek",
    "Conditional Formatting",
    "Entire Chapter"
  ],

  "Networking": [
    "Introduction to Computer Networks",
    "Types of Computer Networks",
    "Protocols and Error Detection",
    "Home Networks and the Internet",
    "Entire Chapter"
  ],

  "Security and Privacy": [
    "Defining Security and Privacy",
    "Threats",
    "Defences",
    "Analysis",
    "Entire Chapter"
  ],

  "Intellectual Property": [
    "Introduction to Intellectual Property",
    "Copyright",
    "Software Licenses",
    "Software Piracy",
    "Copyright Infringement",
    "Entire Chapter"
  ],

  "Impact of Computing": [
    "Impact of Computing on Different Industries",
    "Proliferation of Falsehoods",
    "Entire Chapter"
  ],

  "Emerging Technologies": [
    "Artificial Intelligence",
    "Other Emerging Technologies",
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
          pass
    with col2:
      if st.button("No"):
          st.rerun()



class study_task:
    """
    Access chapter and topics more easily
    Parameters:
    z: user confidence in subtopic
    """
    def __init__(self,x:int,y:int,z:int,comments=None):
        self.x = x
        self.y=y
        self.z = z
        self.comments = comments
    def getitem(self):
        return [chapters[self.x],subtopics[chapters[self.x]][self.y],self.z]
task_list = [study_task(0,0,5).getitem()]
if 'tasklist' not in st.session_state:
    print('activate first')
    st.session_state['tasklist'] = [study_task(0,0,5).getitem()]
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
                    temp.append([task_list[i][0],task_list[i][1],task_list[i][2]]) #Matthias you can optimize this
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
                    task_list = [study_task(0,0,5).getitem()]
                else:
                    #print('THIS SHOULD NOT HAPPEN')
                    task_list.append(study_task(chapters.index(task_list[-1][0]),subtopics[task_list[-1][0]].index(task_list[-1][1]),5).getitem())
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
        
        
