import streamlit as st

st.title("동전 던지기 게임")
st.text("쫄?")
st.divider()  # 가로 긴 줄 구분선

st.image('assets/coin_head.png')
st.image('assets/coin_tail.png')
st.subheader("동전 던지기 게임에 오신 것을 환영합니다^-^")
st.subheader("앞면일까요? 뒷면일까요?")

if st.button("앞면"):
  st.text("진짜?")
if st.button("뒷면"):
  st.text("확실해?")
