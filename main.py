import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

# 장소별 위도/경도 정보
place_coords = {
    "카페거리 (연남동)": [37.5660, 126.9237],
    "홍대 프린트베이커리": [37.5563, 126.9258],
    "디뮤지엄 (성수)": [37.5464, 127.0550],
    "성수 카페거리": [37.5447, 127.0565],
    "서울숲": [37.5444, 127.0370],
    "씨네큐 성수": [37.5442, 127.0547],
    "책읽는 공간 위트앤시니컬": [37.5625, 126.9369],
    "서울책보고": [37.5383, 127.0017],
    "이화 벽화마을": [37.5774, 127.0036],
    "혜화 시집서점": [37.5822, 127.0025],
    "성수동 서울숲길 마켓": [37.5462, 127.0422],
    "언더스탠드 에비뉴": [37.5433, 127.0465],
    "대학로 소극장 거리": [37.5825, 127.0021],
    "낙산공원": [37.5796, 127.0079],
    "홍대 걷고싶은 거리": [37.5573, 126.9245],
    "홍대 프리마켓": [37.5571, 126.9229],
    "롯데월드": [37.5110, 127.0980],
    "석촌호수 레스토랑": [37.5109, 127.1042],
    "더클라이밍 홍대": [37.5565, 126.9225],
    "비건식당 러빙헛": [37.5562, 126.9270],
    "코엑스 아쿠아리움": [37.5125, 127.0592],
    "국립과천과학관": [37.4337, 126.9966],
    "망리단길": [37.5496, 126.9114],
    "서울시립천문대": [37.6039, 127.1043],
    "홍대 VR파크": [37.5553, 126.9239],
    "삼성전자 홍대 플래그십": [37.5551, 126.9234],
    "반포 한강공원": [37.5123, 126.9956],
    "세빛섬 갤러리": [37.5209, 126.9905],
    "서울랜드": [37.4355, 127.0096],
    "남문시장": [37.4352, 127.0176],
    "용산 국립중앙박물관": [37.5230, 126.9804],
    "한남동 레스토랑": [37.5270, 127.0008]
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
    st.markdown(f"#### 📍 추천 장소: {', '.join(match['places'])}")

    for place in match['places']:
        st.markdown(f"##### 🗺️ 장소 지도 보기: **{place}**")
        if place in place_coords:
            lat, lon = place_coords[place]
            map_view = folium.Map(location=[lat, lon], zoom_start=15)
            folium.Marker([lat, lon], popup=place).add_to(map_view)
            st_folium(map_view, width=700, height=400)
        else:
            st.warning(f"위치 정보를 찾을 수 없습니다: {place}")
else:
    st.warning("해당 MBTI에 대한 커플 추천 정보가 아직 없습니다. 🙏")

# 하단 영역
st.markdown("""
---
<center>Made with ❤️ by Streamlit & GPT</center>
""", unsafe_allow_html=True)
