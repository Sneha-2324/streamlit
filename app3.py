import streamlit as st
st.title("make a simple calculator")
num1= st.number_input("Enter first number")
num2= st.number_input("Enter second number")
operation =st.selectbox("choose operatiob ", ["add", "subtract", "multiply", "divide"])
if st.button("calculator"):
    if operation== "add":
        result=num1+num2
    elif operation=="subtarct":
        result= num1-num2
    elif operation== "multiply":
        result=num1*num2
    elif operation== "divide":
        result= num1/num2
    else :
        result=0
                     

st.write("Result", result)