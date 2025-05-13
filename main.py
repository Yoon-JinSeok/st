import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

# MBTI 궁합 추천 및 데이트 코스 + 장소 연결 (장소 2개 이상으로 확장)
mbti_matches = dict(sorted({
    "INTJ": {"match": "ENFP", "reason": "ENFP의 따뜻함과 창의력이 INTJ의 계획적인 성향을 보완해줍니다.", "date": "아날로그 감성 북카페 & 창작 공방 체험 📚🎨", "places": ["카페거리 (연남동)", "홍대 프린트베이커리"]},
    "INTP": {"match": "ESFJ", "reason": "ESFJ의 사교성과 따뜻함이 INTP의 내향적 성향에 활력을 줍니다.", "date": "전시회 데이트 & 디저트 카페 🍰🖼️", "places": ["디뮤지엄 (성수)", "성수 카페거리"]},
    "ENTJ": {"match": "INFP", "reason": "INFP의 감성적인 배려가 ENTJ의 열정과 잘 어우러집니다.", "date": "공원 산책 & 감성 영화관 🎬🌳", "places": ["서울숲", "씨네큐 성수"]},
    "ENTP": {"match": "INFJ", "reason": "INFJ의 이상주의와 ENTP의 에너지가 깊이 있는 소통을 가능하게 합니다.", "date": "북토크 & 즉흥 여행 📚✈️", "places": ["책읽는 공간 위트앤시니컬", "서울책보고"]},
    "INFJ": {"match": "ENFP", "reason": "감성과 이상을 추구하는 INFJ에게 ENFP의 따뜻함이 큰 위로가 됩니다.", "date": "시집 낭독회 & 벽화마을 데이트 🎨📖", "places": ["이화 벽화마을", "혜화 시집서점"]},
    "INFP": {"match": "ENTJ", "reason": "INFP의 이상주의와 ENTJ의 추진력이 좋은 균형을 이룹니다.", "date": "감성 카페 & 마켓 구경 ☕🛍️", "places": ["성수동 서울숲길 마켓", "언더스탠드 에비뉴"]},
    "ENFJ": {"match": "INFP", "reason": "서로에 대한 공감 능력이 뛰어나 따뜻한 관계를 유지합니다.", "date": "소극장 연극 & 야경 산책 🎭🌃", "places": ["대학로 소극장 거리", "낙산공원"]},
    "ENFP": {"match": "INTJ", "reason": "INTJ의 깊은 사고력과 ENFP의 창의성은 훌륭한 시너지를 냅니다.", "date": "보드게임 카페 & 벼룩시장 🧩🛒", "places": ["홍대 걷고싶은 거리", "홍대 프리마켓"]},
    "ISTJ": {"match": "ESFP", "reason": "ESFP의 즉흥성과 ISTJ의 책임감이 상호 보완됩니다.", "date": "테마파크 & 저녁 파스타 데이트 🎢🍝", "places": ["롯데월드", "석촌호수 레스토랑"]},
    "ISFJ": {"match": "ESTP", "reason": "ISFJ의 배려심과 ESTP의 활기찬 성격이 조화를 이룹니다.", "date": "실내 암벽등반 & 건강식 디너 🧗🥗", "places": ["더클라이밍 홍대", "비건식당 러빙헛"]},
    "ESTJ": {"match": "ISFP", "reason": "ESTJ의 조직력과 ISFP의 부드러움이 균형을 이룹니다.", "date": "아쿠아리움 & 자연사 박물관 🐠🏛️", "places": ["코엑스 아쿠아리움", "국립과천과학관"]},
    "ESFJ": {"match": "INTP", "reason": "ESFJ의 감정 표현력과 INTP의 분석력이 서로를 자극합니다.", "date": "맛집 투어 & 별자리 관측 🌌🍜", "places": ["망리단길", "서울시립천문대"]},
    "ISTP": {"match": "ENFJ", "reason": "ENFJ의 따뜻한 관심이 ISTP의 조용한 성향을 끌어냅니다.", "date": "VR 체험 & 플래너 만들기 🎮📓", "places": ["홍대 VR파크", "삼성전자 홍대 플래그십"]},
    "ISFP": {"match": "ESTJ", "reason": "ESTJ의 결단력과 ISFP의 감수성이 잘 맞습니다.", "date": "한강 피크닉 & 갤러리 데이트 🍱🖌️", "places": ["반포 한강공원", "세빛섬 갤러리"]},
    "ESTP": {"match": "ISFJ", "reason": "ISFJ의 따뜻함과 ESTP의 모험심이 잘 어울립니다.", "date": "카트레이싱 & 야시장 구경 🏎️🌮", "places": ["서울랜드", "남문시장"]},
    "ESFP": {"match": "ISTJ", "reason": "ISTJ의 안정감이 ESFP의 감정 표현을 잘 수용합니다.", "date": "박물관 & 고급 다이닝 데이트 🏺🍽️", "places": ["용산 국립중앙박물관", "한남동 레스토랑"]},
}.items()))

# 추천 장소 목록 (서울)
seoul_places = {
    "카페거리 (연남동)": [37.5647, 126.9220],
    "디뮤지엄 (성수)": [37.5463, 127.0537],
    "서울숲": [37.5444, 127.0370],
    "책읽는 공간 위트앤시니컬": [37.5610, 126.9370],
    "이화 벽화마을": [37.5776, 127.0046],
    "성수동 서울숲길 마켓": [37.5445, 127.0560],
    "대학로 소극장 거리": [37.5816, 127.0026],
    "홍대 걷고싶은 거리": [37.5572, 126.9228],
    "롯데월드": [37.5110, 127.0980],
    "더클라이밍 홍대": [37.5550, 126.9206],
    "코엑스 아쿠아리움": [37.5126, 127.0592],
    "망리단길": [37.5494, 126.9063],
    "홍대 VR파크": [37.5555, 126.9233],
    "반포 한강공원 & 세빛섬 갤러리": [37.5123, 126.9957],
    "서울랜드 & 남문시장": [37.4363, 127.0105],
    "용산 국립중앙박물관 & 한남동 레스토랑": [37.5231, 126.9809],
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
    st.markdown(f"#### 💑 추천 데이트 코스: {match['date']} (추천 장소: {match['place']})")

    # 장소 출력
    place = match.get("place")
    if place and place in seoul_places:
        st.markdown(f"#### 🗺️ 추천 장소 지도: **{place}**")
        lat, lon = seoul_places[place]
        map_view = folium.Map(location=[lat, lon], zoom_start=15)
        folium.Marker([lat, lon], popup=f"{place} - {match['date']}").add_to(map_view)
        st_folium(map_view, width=700, height=500)
else:
    st.warning("해당 MBTI에 대한 커플 추천 정보가 아직 없습니다. 🙏")

# 하단 영역
st.markdown("""
---
<center>Made with ❤️ by Streamlit & GPT</center>
""", unsafe_allow_html=True)
