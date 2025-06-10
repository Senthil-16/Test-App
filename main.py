import streamlit as st
from streamlit_option_menu import option_menu
st.title("😎Vinsup Infotech")
# with st.sidebar:
#     st.header("Vinsup Infotech")

# st.write("- Welcome To Infotech🎈")
# st.write("# Data Science🤖🧠🇦🇮👾s")
# st.write("## Data Science Is Future")
# st.write("_streamlit🌐_")
# st.text_input("Enter Your Name")
# st.button("Submit")

with st.sidebar:
    data = option_menu(
        menu_title="Data Science",
        options=["Home","About","Things To Know"],
        icons=["house-heart-fill","file-person","question-square"]

    )
if data == "Home":
    st.header("Registration Form")
    col1,col2 = st.columns(2)
    with col1:
         Name = st.text_input("Enter Your Name")
         Email = st.text_input("Enter Your Email")
         Gender =  st.radio(label=":rainbow[Select Your Gender]",options=["Male","Female"])
         st.file_uploader("Upload Your Resume")

    with col2:
         Phone = st.text_input("Enter Your Number")
         Password = st.text_input("Enter Your Password")
         City = st.selectbox("City",options=["Madurai","Kovai Pradesh","Chennai"])
         st.metric(label="Python",value=20,delta="20%")
    
    if st.button("Submit"):
        st.write(Name,Email,Phone,Password)
        st.success("Data Inserted Sucessfully")
    
    st.number_input("Integer",max_value=22)
    st.slider("Rate Your Experience",0,100)
    
    



elif data == "About":
    st.header("About Page")
elif data == "Things To Know":
    st.header("Things To Know Page")