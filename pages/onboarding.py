import streamlit as st
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container
st.set_page_config(page_title="Onboarding",layout='wide')

st.markdown("""
<style>
.stApp{
            background-image: linear-gradient(to bottom,#CD63A9B3,#2A5B9B)
            }
</style>

""",unsafe_allow_html=True)

col1,col2,col3, = st.columns([2,10,2])
with col2:
    con = st.container(width='stretch')
    with con:
        st.markdown("""
            <h1 style='color:white'r>
                &nbsp;&nbsp;&nbsp;Welcome To Lyra!
            </h1>
            <p id='id1'>GET STARTED SETTING UP YOUR ACCOUNT</p>
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
                    height:500px;
                    border-radius:25px;
                    justify-content:left;
                    padding:50px;
                    background:#e6e6e6;
                    }
                     """):
            name = st.text_input('Enter your name: ',width=400)
            st.empty()
            st.text('')
            if st.button('Continue:'):
                st.switch_page("./pages/home.py")
        # st.markdown("""
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
        
        
