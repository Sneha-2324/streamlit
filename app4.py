import streamlit as st
import google.generativeai as genai
st.title("welcome to my streamlit")
user_input = st.text_input("ASK ME ANYTHING")
genai.configure(api_key= "AIzaSyCxdJmsv3z4SSZxeNRqg-xwnkWC3K35utQ")

models= genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
    response= models.generate_content(user_input)
    st.write("response" ,response.text)