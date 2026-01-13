import streamlit as st
st.title("some basic command in streamlit")

name=st.text_input("Enetr your name: ")
if st.button("Submit"):
    st.write("hello" , name)
  