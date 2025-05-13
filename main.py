import streamlit as st
from PIL import Image

# MBTI to job mapping dictionary
mbti_jobs = {
    "INTJ": ["전략 컨설턴트 💼", "데이터 과학자 📊", "AI 연구원 🤖"],
    "INFP": ["작가 ✍️", "상담사 💬", "예술가 🎨"],
    "ENTP": ["기업가 🚀", "마케터 📣", "방송인 🎙️"],
    "ISFJ": ["간호사 👩‍⚕️", "교사 👩‍🏫", "사회복지사 ❤️"],
    # ... 나머지 유형 추가 가능
}

# Streamlit 앱 설정
st.set_page_config(page_title="MBTI 직업 추천기 💡", page_icon="🧠", layout="wide")

# 헤더 영역
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>✨ MBTI 기반 진로 추천 웹앱 ✨</h1>
    <h3 style='text-align: center;'>당신의 성격 유형에 맞는 직업을 알아보세요! 🌟</h3>
""", unsafe_allow_html=True)

# 사이드바 설정
st.sidebar.header("📌 사용 방법")
st.sidebar.write("MBTI 유형을 선택하면 추천 직업이 나와요!")
selected_mbti = st.sidebar.selectbox("당신의 MBTI 유형은 무엇인가요? 🧬", list(mbti_jobs.keys()))

# 메인 콘텐츠
st.markdown("""
<div style='text-align: center;'>
    <img src='https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif' width='300'>
</div>
""", unsafe_allow_html=True)

st.markdown(f"## 🧠 당신의 MBTI 유형은 **:rainbow[{selected_mbti}]**!")

if selected_mbti in mbti_jobs:
    st.markdown("### 🌈 추천 직업 리스트:")
    cols = st.columns(3)
    for i, job in enumerate(mbti_jobs[selected_mbti]):
        with cols[i % 3]:
            st.success(f"{job}")
else:
    st.warning("해당 MBTI에 대한 추천 정보가 아직 없습니다. 🙏")

# 하단 영역
st.markdown("""
---
<center>Made with ❤️ by Streamlit & GPT</center>
""", unsafe_allow_html=True)
