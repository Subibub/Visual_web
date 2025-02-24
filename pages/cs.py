import streamlit as st
from navigation import load_navbar  # 공통 네비게이션 바 불러오기
from login_handler import init_login_state, handle_login, handle_logout # 로그인 처리 함수 불러오기
import time
import json
import os
from streamlit_lottie import st_lottie


st.set_page_config(page_title="고객센터-LendSure", page_icon="📞", layout="wide")

# 로그인 상태 초기화
init_login_state()

if st.session_state["logged_in"]:
    st.title(f"{st.session_state['username']}님, 환영합니다! 🚀")
else:
    st.title("환영합니다! 로그인해 주세요.")
# 네비게이션 바 로드
load_navbar()  

# 로그인 / 로그아웃 처리
handle_login()
handle_logout()

#================================================================================================#
# 스타일 커스텀: 폰트, 버튼, 레이아웃 개선
st.markdown(
    """
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
        }
        .contact-header {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .contact-description {
            text-align: center;
            font-size: 16px;
            color: #666;
            margin-bottom: 30px;
        }
        .service-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-bottom: 40px;
        }
        .service-box {
            text-align: center;
            width: 200px;
        }
        .service-icon {
            font-size: 40px;
            margin-bottom: 10px;
            display: block;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 40px;
        }
        .phone-table {
            width: 100%;
            text-align: center;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        .phone-table th, .phone-table td {
            border-bottom: 1px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }
        .phone-table th {
            background: #f8f8f8;
        }
        .call-button {
            display: block;
            text-align: center;
            background-color: #58ACFA;
            color: white !important;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            text-decoration: none;
            width: 250px;
            margin: 0 auto;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            transition: 0.3s;
        }
        .call-button:hover {
            background-color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 헤더
st.markdown("<div class='contact-header'>📞 렌드슈어 상담센터</div>", unsafe_allow_html=True)
st.markdown("<div class='contact-description'>고객님의 금융 관련 상담 및 문의사항 해결을 위해 최선을 다하겠습니다.</div>", unsafe_allow_html=True)

# 상담 서비스 섹션
st.markdown("""
<div class="service-container">
    <div class="service-box">
        <span class="service-icon">📧</span>
        <p><b>이메일 상담</b></p>
        <p>365일 24시간</p>
    </div>
    <div class="service-box">
        <span class="service-icon">💬</span>
        <p><b>실시간 채팅 상담</b></p>
        <p>평일 09:00 ~ 22:00</p>
    </div>
    <div class="service-box">
        <span class="service-icon">🖥</span>
        <p><b>원격 지원 상담</b></p>
        <p>평일 09:00 ~ 18:00</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 전화번호 안내 테이블
st.markdown("""
<table class="phone-table">
    <tr>
        <th>고객센터</th>
        <th>대출</th>
        <th>투자</th>
    </tr>
    <tr>
        <td>1599-1111</td>
        <td>1599-2222</td>
        <td>1599-4567</td>
    </tr>
</table>
""", unsafe_allow_html=True)

# 전화 상담 버튼
st.markdown('<a href="tel:15991111" class="call-button">📞 전화 상담 예약 09:00 ~ 18:00</a>', unsafe_allow_html=True)