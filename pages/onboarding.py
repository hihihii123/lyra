import streamlit as st
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container
st.set_page_config(page_title="Onboarding",layout='wide')


col1,col2,col3, = st.columns([1,10,1])
with col2:
    con = st.container(width='stretch')
    with con:
        st.markdown("""
                    <h1>
                     &nbsp;&nbsp;&nbsp;Welcome To Lyra!
                    </h1>
                    <p>GET STARTED SETTING UP YOUR ACCOUNT</p>
                    <div id="boxid">
                    </div>
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
                    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
                    h1{
                    text-align:center;
                    font-family: 'Comic';sans-serif;
                    }
                    p{
                    text-align:center;
                    font-family: 'Inter';sans-serif;
                    }
                    #boxid{
                    width:500px;
                    height:500px;
                    border:1px solid #0000ff;
                    justify-content:center;
                    padding:50px;
                    }
                    </style>
                    """
                    ,unsafe_allow_html=True)
        
        
        st.header('Welcome to Lyra!',text_alignment='center')
