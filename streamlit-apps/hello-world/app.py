import streamlit as st

st.title("Hello World! 👋")
st.write("My first Streamlit Cloud app")

name = st.text_input("What's your name?")
if name:
    st.balloons()
    st.write(f"Hello, {name}!")
