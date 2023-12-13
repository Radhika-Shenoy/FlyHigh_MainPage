import streamlit as st 
#st.set_page_config(layout="wide")
image1_url = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1699276263998-e77dd2e1b1b6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcwMTc5MzYzNQ&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080');
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>
    '''
st.markdown(image1_url, unsafe_allow_html=True)

st.markdown('<h1 style="color:black;font-size:35px;text-align:left;margin-left:20px;">FlyHigh Airlines</h1>', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('<p style="color:black; font-weight:bold;">FlyHigh provides 2 login options catering to member specific needs</p>', unsafe_allow_html=True)
    expander1 = st.expander("Manager Login Info")
    with expander1:
        st.write("If you are the Manager at the FlyHigh team then enter your credentials on the Manager login tab provided on the right! ")
        st.warning("Hover on the Help icon next to the input box for using default username/password")
    expander2 = st.expander("R&D member Login Info")
    with expander2:
        st.write("If you are a member from the FlyHigh R&D team then enter your admin credentials on the R&D member login tab provided on the right! ")
        st.warning("Hover on the Help icon next to the input box for using default username/password")
tab1, tab2,tab3 = st.tabs(['Manager Login', 'R&D Member Login','Bio'])


with tab1:
    #st.markdown('<p style="color:black; font-weight:bold;">Manager Login</p>', unsafe_allow_html=True)
#Login form for initial login page
    #with st.sidebar:
    with st.form(key='login_form1'):
        st.subheader('Login Credentials')
        username = st.text_input('**Enter your FlyHigh userID:**',help='Default username: user')       
        password = st.text_input('**Enter your FlyHigh password:**', type='password',help='Default password: password')
        
        st.markdown('<p style="color:black; font-weight:bold;">Disclaimer!</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:black; font-weight:bold;">Certain sections of the web app contain sensitive FlyHigh brand data and passenger survey information. Kindly refrain from accessing this information if you are not an authorized FlyHigh team member. Unauthorized access will be subject to penalties.</p>', unsafe_allow_html=True)
        checkbox_val = st.checkbox("**I am an employed FlyHigh member**") 
        login_button = st.form_submit_button('Login')
        if login_button:
            if not username or not password:
                st.error("Please enter the credentials to login")
        if login_button:
            if username and password:
                # Based on the credentials login is redirected
                if not (username == 'user' and password == 'password'):
                    st.error("Invalid username/ password")
                if (username == 'user' and password == 'password'):
                    if not checkbox_val:
                        st.error('Please accept that you are an employeed FlyHigh member')
                    if checkbox_val:
                        if login_button:
                            st.success('Login Successful!')
                            st.markdown(f'<a href="https://flyhighmanager-uwrq7ugrkozw5muz23tugg.streamlit.app"><button>Go to the Authorised Manager website</button></a>', unsafe_allow_html=True)                  
with tab2:      
    #st.markdown('<p style="color:black; font-weight:bold;">R&D member login</p>', unsafe_allow_html=True) 
    if tab2:        
       # with st.sidebar:
        st.markdown('<p style="color:black; font-weight:bold;">Disclaimer: Login access only for a member on the R&D team</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:black; font-weight:bold;">Please login to view high level visualization</p>', unsafe_allow_html=True)
        with st.form(key='login_form2'):
            st.subheader('Login Credentials')
            username = st.text_input('**Enter your FlyHigh admin userID:**',help='Default username: adminuser')
            #st.markdown('Default username: adminuser')
            password = st.text_input('**Enter your FlyHigh admin password:**', type='password',help='Default password: adminpwd')
            #st.markdown('Default password: adminpwd')
            checkbox_val = st.checkbox("**I am an authorized FlyHigh member from the R&D team and wish to view the high dimensional representation of features!**")
            login_button = st.form_submit_button('Login')
        if login_button:
            if username == 'adminuser' and password == 'adminpwd':               
                if not checkbox_val:
                    st.error("Please agree that you are an authorized FlyHigh R&D team member prior to login")
                if checkbox_val:
                    st.success("Login successful!")
                    st.markdown(f'<a href="https://flyhighrd-4svp9q5k7hdshtpq77oecp.streamlit.app"><button>Go to the Authorised R&D website</button></a>', unsafe_allow_html=True)                  

            else:
                st.error("Invalid username/ password")
with tab3:
    col1,col2 = st.columns([3,3])
    with col1: 
        st.image("bio_image.jpg")
    with col2:
        st.markdown('<p style="text-align:justify;font-weight:bold;">Welcome to my Bio Tab! This section offers a glimpse into my world. I\'m currently pursuing a Master\'s in Data Science at MSU, driven by a passion for analyzing and interpreting data. Alongside my academic journey, I indulge in various interests; traveling allows me to explore diverse cultures, cooking diverse cuisines broadens my culinary skills, and practicing yoga helps me maintain a balanced lifestyle. My skills span Python, Data Analysis, and Machine Learning, fueling my enthusiasm for learning new technologies.',unsafe_allow_html = True)

    

    

                
