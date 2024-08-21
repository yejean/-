import streamlit as st

st.title("Hello")
st.header("Welcome to my website!")
st.subheader("환영합니다~!")

Clicked = st.button("시작하기")
if Clicked :
  st.write("짠")
