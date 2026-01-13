import streamlit as st
st.title("some basic command like slider button etc")
age= st.slider("Enter your age" , 1, 100)
city= st.selectbox("Choose your city" , ["delhi", "mumbai", "pune", "baramati"])
if st.button("Show details"):
    st.write("age", age)
    st.write("city", city)

