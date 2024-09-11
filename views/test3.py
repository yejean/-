import streamlit as st

st.title("스트림릿 테스트 3")

st.divider()  # 가로 긴 줄 구분선

# password 인자 활용
string = st.text_input(
    'I love you',
    placeholder='write down your favorite person's name',
    type='password'
)

if string:
    st.text('Your love is '+string)
