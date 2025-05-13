import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

# MBTI 궁합 추천 및 데이트 코스 + 장소 연결
mbti_matches = {
    "INTJ": {"match": "ENFP", "reason": "ENFP의 따뜻함과 창의력이 INTJ의 계획적인 성향을 보완해줍니다.", "date": "아날로그 감성 북카페 & 창작 공방 체험 📚🎨", "place": "북촌 한옥마을"},
    "INTP": {"match": "ESFJ", "reason": "ESFJ의 사교성과 따뜻함이 INTP의 내향적 성향에 활력을 줍니다.", "date": "전시회 데이트 & 디저트 카페 🍰🖼️", "place": "DDP (동대문디자인플라자)"},
    "ENTJ": {"match": "INFP", "reason": "INFP의 감성적인 배려가 ENTJ의 열정과 잘 어우러집니다.", "date": "공원 산책 & 감성 영화관 🎬🌳", "place": "서울숲"},
    "ENTP": {"match": "INFJ", "reason": "INFJ의 이상주의와 ENTP의 에너지가 깊이 있는 소통을 가능하게 합니다.", "date": "북토크 & 즉흥 여행 📚✈️", "place": "경복궁"},
    "INFJ": {"match": "ENFP", "reason": "감성과 이상을 추구하는 INFJ에게 ENFP의 따뜻함이 큰 위로가 됩니다.", "date": "시집 낭독회 & 벽화마을 데이트 🎨📖", "place": "북촌 한옥마을"},
    "INFP": {"match": "ENTJ", "reason": "INFP의 이상주의와 ENTJ의 추진력이 좋은 균형을 이룹니다.", "date": "감성 카페 & 마켓 구경 ☕🛍️", "place": "한강 반포공원"},
    "ENFJ": {"match": "INFP", "reason": "서로에 대한 공감 능력이 뛰어나 따뜻한 관계를 유지합니다.", "date": "소극장 연극 & 야경 산책 🎭🌃", "place": "남산타워"},
    "ENFP": {"match": "INTJ", "reason": "INTJ의 깊은 사고력과 ENFP의 창의성은 훌륭한 시너지를 냅니다.", "date": "보드게임 카페 & 벼룩시장 🧩🛒", "place": "서울숲"},
    "ISTJ": {"match": "ESFP", "reason": "ESFP의 즉흥성과 ISTJ의 책임감이 상호 보완됩니다.", "date": "테마파크 & 저녁 파스타 데이트 🎢🍝", "place": "한강 반포공원"},
    "ISFJ": {"match": "ESTP", "reason": "ISFJ의 배려심과 ESTP의 활기찬 성격이 조화를 이룹니다.", "date": "실내 암벽등반 & 건강식 디너 🧗🥗", "place": "서울숲"},
    "ESTJ": {"match": "ISFP", "reason": "ESTJ의 조직력과 ISFP의 부드러움이 균형을 이룹니다.", "date": "아쿠아리움 & 자연사 박물관 🐠🏛️", "place": "DDP (동대문디자인플라자)"},
    "ESFJ": {"match": "INTP", "reason": "ESFJ의 감정 표현력과 INTP의 분석력이 서로를 자극합니다.", "date": "맛집 투어 & 별자리 관측 🌌🍜", "place": "남산타워"},
    "ISTP": {"match": "ENFJ", "reason": "ENFJ의 따뜻한 관심이 ISTP의 조용한 성향을 끌어냅니다.", "date": "VR 체험 & 플래너 만들기 🎮📓", "place": "DDP (동대문디자인플라자)"},
    "ISFP": {"match": "ESTJ", "reason": "ESTJ의 결단력과 ISFP의 감수성이 잘 맞습니다.", "date": "한강 피크닉 & 갤러리 데이트 🍱🖌️", "place": "한강 반포공원"},
    "ESTP": {"match": "ISFJ", "reason": "ISFJ의 따뜻함과 ESTP의 모험심이 잘 어울립니다.", "date": "카트레이싱 & 야시장 구경 🏎️🌮", "place": "남산타워"},
    "ESFP": {"match": "ISTJ", "reason": "ISTJ의 안정감이 ESFP의 감정 표현을 잘 수용합니다.", "date": "박물관 & 고급 다이닝 데이트 🏺🍽️", "place": "경복궁"},
}

# 추천 장소 목록 (서울)
seoul_places = {
    "북촌 한옥마을": [37.5826, 126.9830],
    "서울숲": [37.5444, 127.0370],
    "한강 반포공원": [37.5123, 126.9957],
    "DDP (동대문디자인플라자)": [37.5665, 127.0095],
    "남산타워": [37.5512, 126.9882],
    "경복궁": [37.5796, 126.9770]
}

# Streamlit 앱 설정
st.set_page_config(page_title="MBTI 커플 궁합 추천 💘", page_icon="💑", layout="wide")

# 헤더 영역
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>💞 MBTI 궁합 추천 웹앱 💞</h1>
    <h3 style='text-align: center;'>당신의 성격 유형에 맞는 최고의 커플 매칭을 알아보세요! 🌟</h3>
""", unsafe_allow_html=True)

# 사이드바 설정
st.sidebar.header("📌 사용 방법")
st.sidebar.write("MBTI 유형을 선택하면 궁합 좋은 커플 유형과 데이트 코스를 추천해줘요!")
selected_mbti = st.sidebar.selectbox("당신의 MBTI 유형은 무엇인가요? 🧬", list(mbti_matches.keys()))

# 메인 콘텐츠
st.markdown("""
<div style='text-align: center;'>
    <img src='https://media.giphy.com/media/26FPpP8K0vBSF7rNu/giphy.gif' width='300'>
</div>
""", unsafe_allow_html=True)

st.markdown(f"## 💌 당신의 MBTI는 **:rainbow[{selected_mbti}]**!")

if selected_mbti in mbti_matches:
    match = mbti_matches[selected_mbti]
    st.markdown(f"### 💘 가장 잘 어울리는 커플 유형: **{match['match']}**")
    st.markdown(f"#### 💡 이유: {match['reason']}")
    st.markdown(f"#### 💑 추천 데이트 코스: {match['date']}")

    # 장소 출력
    place = match.get("place")
    if place and place in seoul_places:
        st.markdown(f"#### 🗺️ 추천 장소: **{place}**")
        lat, lon = seoul_places[place]
        map_view = folium.Map(location=[lat, lon], zoom_start=15)
        folium.Marker([lat, lon], popup=place).add_to(map_view)
        st_folium(map_view, width=700, height=500)
else:
    st.warning("해당 MBTI에 대한 커플 추천 정보가 아직 없습니다. 🙏")

# 하단 영역
st.markdown("""
---
<center>Made with ❤️ by Streamlit & GPT</center>
""", unsafe_allow_html=True)
