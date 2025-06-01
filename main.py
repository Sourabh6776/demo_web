import streamlit as st
st.title("Welcome to SOURABH RATHORE ")

name = st.text_input("Enter your name : ")
father_name = st.text_input("Enter your Father name : ")
adress = st.text_input("Enter your adress : ")
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6))
button = st.button("Done")
if button :
    st.markdown(f"""
 Name : {name}
Father Name : {name}
adress : {adress}
class : {classdata}""")