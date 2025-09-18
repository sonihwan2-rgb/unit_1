import streamlit as st  # Streamlit 라이브러리 임포트
from PIL import Image  # 이미지 처리를 위한 PIL 임포트
import requests  # 이미지 다운로드를 위한 requests 임포트
from io import BytesIO  # 이미지 바이트 처리


st.set_page_config(page_title="AI 자연환경 사진 갤러리", layout="centered")  # 페이지 설정
st.title("AI로 만든 자연환경 사진 갤러리")  # 페이지 타이틀
st.write("아래는 AI로 생성된 자연환경 사진과 실제 모티브가 된 장소의 구글 맵 위치입니다.")  # 설명 텍스트

# 예시 데이터: 사진 URL과 장소 정보
photos = [
    {
        "title": "알프스 산맥의 아침",
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",  # AI 생성 이미지 예시
        "location": "알프스 산맥, 스위스",
        "maps_query": "Alps, Switzerland"
    },
    {
        "title": "아마존 열대우림",
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "location": "아마존, 브라질",
        "maps_query": "Amazon Rainforest, Brazil"
    },
    {
        "title": "사하라 사막의 일몰",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=800&q=80",
        "location": "사하라 사막, 아프리카",
        "maps_query": "Sahara Desert, Africa"
    }
]

for photo in photos:
    st.subheader(photo["title"])  # 사진 제목
    # 이미지 다운로드 및 표시
    try:
        response = requests.get(photo["image_url"])  # 이미지 URL에서 다운로드
        img = Image.open(BytesIO(response.content))  # 바이트 데이터를 이미지로 변환
        st.image(img, use_column_width=True, caption=photo["location"])  # 이미지와 캡션 표시
    except Exception as e:
        st.error(f"이미지를 불러올 수 없습니다: {e}")  # 오류 처리

    # 구글 맵 링크 생성 및 표시
    maps_url = f"https://www.google.com/maps/search/?api=1&query={photo['maps_query'].replace(' ', '+')}"  # 구글 맵 검색 URL 생성
    st.markdown(f"[구글 맵에서 위치 보기]({maps_url})", unsafe_allow_html=True)  # 구글 맵 링크 표시
    st.markdown("---")  # 구분선
