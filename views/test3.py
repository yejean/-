import streamlit as st
import random

# 게임 결과 내는 함수, guessNum는 사람 추측값(0:앞면, 1:뒷면)
st.title("동전 던지기 게임")
st.text("쫄?")
st.divider()  # 가로 긴 줄 구분선

col1, col2 = st.columns(2)
col1.write('동전 앞면')
col2.write('동전 뒷면')

with col1:
    st.image('assets/coin_head.png')
with col2:
    st.image('assets/coin_tail.png')

st.subheader("동전 던지기 게임에 오신 것을 환영합니다^-^")

computer = random.randint(0, 1)    # 컴퓨터 숫자 (0 앞면, 1 뒷면)
st.subheader("앞면일까요? 뒷면일까요?")

choice = -1    # 사용자 숫자 (초기값은 선택 안함을 의미하는 -1)

if st.button("앞면"):
    choice = 0    # 사용자가 동전 앞면을 선택하면 0
if st.button("뒷면"):
    choice = 1    # 사용자가 동전 뒷면을 선택하면 1

if choice != -1:  # 사용자가 동전 선택을 한 경우
  st.divider()  # 가로 긴 줄 구분선
  col3, col4 = st.columns(2)
  col3.write('동전 결과 : ')
  col4.write('나의 선택 : ')
    
  with col3:
      if computer == 0:
        st.image('assets/coin_head.png')
      else:
        st.image('assets/coin_tail.png')
            
  with col4:
      if choice == 0:
        st.image('assets/coin_head.png')
      else:
        st.image('assets/coin_tail.png')
    
  if computer == choice:
    st.subheader("적중!!")
    st.balloons()
  else:
    st.subheader("이걸 틀리네 ㅋ")
    
    st.button("다시 하기")
