import streamlit as st
from navigation import load_navbar  # 공통 네비게이션 바 불러오기
from login_handler import init_login_state, handle_login, handle_logout # 로그인 처리 함수 불러오기
import json
import os
from streamlit_lottie import st_lottie
import time


# 페이지 기본 설정
st.set_page_config(page_title="LendSure", layout="wide", page_icon="🛡️",initial_sidebar_state="collapsed")

# 로그인 상태 초기화
init_login_state()

# 네비게이션 바 로드
load_navbar()  

# 로그인 / 로그아웃 처리
handle_login()
handle_logout()



#----------------------------------------------------------
# CSS 스타일 적용 (스크롤 가능한 섹션 UI)
st.markdown("""
    <style>   
        html, body {
            font-family : "Poppins'. sans-serif;
            scroll-snap-type: y mandatory;
            overflow-y: scroll;
            height: 100vh;
            scroll-behavior: smooth;
            margin: 0;
        }
        .top-bg {
            text-align: center;
            padding: 80px 20px;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
    
        }
        .top-bg h1 {
            font-family:"Alegreya", serif;
            font-size: 80px;
            font-weight: bold;
            color: #08298A;
            margin-bottom: 15px;
        }
        .top-bg p {
            font-style: normal;
            font-size: 26px;
            color:gray;
            margin-top: 0;
            margin-bottom: 25px;
        }
        .top-bg a {
            background-color: #0F4C75;
            padding: 18px 35px;
            color: white;
            text-decoration: none;
            font-size: 22px;
            border-radius: 25px;
            transition: background-color 0.3s ease-in-out;
        }
        .top-bg a:hover {
            background-color: #BBE1FA;
        }
        [data-testid="stHeaderActionElements"] {
            display: none !important;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 10px;
            margin-top: -40px; /* 중앙보다 살짝 위로 이동 */
        }
        .subtitle {
            font-size: 18px;
            color: #666;
            max-width: 600px;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .right-section {
            flex: 1;
            text-align: left;
        }
        .button {
            background-color: #0F4C75;
            color: white;
            font-size: 18px;
            padding: 12px 25px;
            border-radius: 25px;
            text-decoration: none;
            display: inline-block;
            border: none;
            cursor: pointer;
            margin-bottom: 50px; /* "렌딧의 현재"와 간격 추가 */
        }
        .button-container {
            margin-top: 10px;
        }
        .section {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
        }
        .container {
            display: flex;
            justify-content: space-between;
            align-items: center; /* 세로 가운데 정렬 */
            padding: 20px
        }
        .animation-container {
            flex: 1;
            display: flex;
            justify-content: flex-start; /* 왼쪽 정렬 */
            align-items: center;
            align-self: flex-start; /* 컨테이너 내에서 왼쪽 정렬 */
        }
        .animation-container canvas {
            max-width: 600px;
            height: auto;
            margin-left: 0 !important; /* 중앙 정렬을 강제로 해제하고 왼쪽 정렬 */
        }
        .left-section {
            flex: 1; /* 왼쪽 섹션의 너비 */
            display: flex;
            justify-content: flex-start; /* 왼쪽 정렬 */
            align-items: center; /* 이미지 세로 가운데 정렬 */
        }
        .button {
            background-color: #0F4C75;
            color: white;
            font-size: 18px;
            padding: 12px 25px;
            border-radius: 25px;
            text-decoration: none;
            display: inline-block;
            border: none;
            cursor: pointer;
            margin-bottom: 50px; /* "렌딧의 현재"와 간격 추가 */
        }
        .button-container {
            margin-top: 10px;
        }
        .big-font {
            font-size:50px !important;
            font-weight: bold;
            text-align: center;
        }
        .sub-text {
            font-size:20px;
            text-align: center;
        }
        .circle-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 30px;
        }
        .circle {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 30px;
            font-weight: bold;
            color: white;
        }
        .green {
            background-color: #088A4B;
            margin-right: 20px;
        }
        .blue {
            background-color: #5a9de5;
            margin-left: 20px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 18px;
            color: gray;
        }
        
        
    </style>
""", unsafe_allow_html=True)
    

#-----------------------------------------페이지 구성 요소--------------------------------------------#
# --------------상단 섹션: 회사 정보 (회사명 & 슬로건)------------------#
# 상단 섹션 : 회사 정보 (회사명 & 슬로건)
st.markdown("""
    <div id="top" class="section top-bg">
        <h1>LendSure</h1>
        <p>신뢰할 수 있는 금융 파트너, 당신과 함께합니다.</p>
        <a href="loan_product" class="nav-link">대출 상품 보기</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------중단 섹션------------------#
col1, col2 = st.columns(2)

with col1:
    st.image("data/invest.png", use_container_width=True)

# Right column: text
with col2:
    st.markdown("## 분산투자를 통한 안정적인 투자")
    st.markdown("렌드슈어에서는 분산투자가 가능하여\n투자의 안정성과 수익성이 높아집니다.")
    st.markdown("적은 금액으로도 다수의 대출 건에 분산 투자하여 효율적으로 포트폴리오를 구축할 수 있습니다.") 


# Custom CSS for styling
st.markdown("""
    <style>
        h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        
        .stButton > button {
            background-color: #0F4C75;
            color: white;
            font-size: 18px;
            padding: 12px 25px;
            border-radius: 25px;
            text-decoration: none;
            display: inline-block;
            border: none;
            cursor: pointer;
            margin-bottom: 50px; /* "렌딧의 현재"와 간격 추가 */
        }
    </style>
""", unsafe_allow_html=True)
# --------------하단 섹션: 회사 성장 데이터------------------#
# 제목
st.markdown("<br><br>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

st.markdown('<p class="big-font">렌드슈어의 현재</p>', unsafe_allow_html=True)

# 원형 통계
st.markdown(
    """
    <div class="circle-container">
        <div class="circle green">2,826억원<br>대출지급</div>
        <div class="circle blue">302만건<br>대출승인</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
# 날짜 정보
st.markdown('<p class="footer">렌드슈어 내부 데이터 기준 (2025년 2월 23일)</p>', unsafe_allow_html=True)
st.markdown('<p class = "sub-text">더 나은 금융을 향해, 렌드슈어는 오늘도 도전합니다.</p>', unsafe_allow_html=True)



st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
# 하단 화면 - 회사 소개 및 고객 지원
st.markdown('<p class="footer">고객센터: 1234-1234 | E-mail: support@LSB.co.kr</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">대표: 이수빈 | 사업자등록번호: 123-123-123</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">ⓒ PFC Technologies All rights reserved.</p>', unsafe_allow_html=True)
