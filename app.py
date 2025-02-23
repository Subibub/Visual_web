import streamlit as st
import json
import os
from streamlit_lottie import st_lottie



# 페이지 기본 설정
st.set_page_config(page_title="LendingClub", layout="wide")

# 초기 세션 상태 설정
if "show_login" not in st.session_state:
    st.session_state.show_login = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Lottie 애니메이션 로드 함수
def load_lottie(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"파일을 찾을 수 없습니다: {filepath}")
        return None

# JSON 파일 로드 (data 폴더 안의 animation.json 파일 사용)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "animation.json")
lottie_animation = load_lottie(FILE_PATH)

# CSS 스타일 적용 (스크롤 가능한 섹션 UI)
st.markdown("""
    <style>   
        html, body {
            scroll-snap-type: y mandatory;
            overflow-y: scroll;
            height: 100vh;
            scroll-behavior: smooth;
            margin: 0;
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
        .middle {
            padding-top: 0;
            height: auto;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 30px 0;
        }
        .left-section {
            width: 40%;
            text-align: left;
        }
        .right-section {
            width: 40%;
            text-align: left;
        }
        .title {
            font-size: 30px;
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
        .button {
            background-color: #1E40AF;
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
        .cards {
            display: flex;
            gap: 20px;
            justify-content: center;
            width: 55%;
        }
        .card {
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            width: 200px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .card-title {
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }
        .card-subtitle {
            font-size: 16px;
            color: #666;
            margin-top: 5px;
        }
        .card:hover {
            transform: translateY(-10px);
        }
        .top-bg {
            background-color: white;
            color: black;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .bottom-section {
            height: 100vh;
            background-color: #2E9AFE;
            color: white;
            padding: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .content-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 90%;
            max-width: 1200px;
        }
        .bottom-left {
            font-size: 42px;
            font-weight: bold;
            color: #222;
            margin-right: 50px;
        }
        .bottom-right {
            flex-grow: 1;
            display: flex;
            align-items: center;
        }
        .stat-item {
            display: flex;
            align-items: center;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .stat-icon {
            width: 50px;
            height: 50px;
            margin-right: 15px;
        }
        .stat-text {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        #dynamic-stats {
            display: inline-block;
        }
        .stMarkdown {
            display: inline-block !important;
        }
        .stColumn {
            padding: 0 !important;
        }
        .stat-content {
            display: flex;
            flex-direction: column;
        }
        .stat-value {
            font-size: 32px;
            font-weight: bold;
            color: #ffffff;
        }
        .stat-label {
            font-size: 16px;
            color: #ffffff;
        }
        .footer {
            text-align: center; margin-top: 60px; font-size: 14px; color: #585858;
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
            background-color: #4cc9a2;
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
        .animation-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        
    </style>
""", unsafe_allow_html=True)

#--------------네비게이션 바------------------#
st.markdown(f"""
    <style>
        /* 네비게이션 바 스타일 */
        .navbar {{
            display: flex;
            justify-content: space-between; /* 로고와 메뉴 양쪽 정렬 */
            align-items: center;
            background-color: black;
            padding: 15px 30px;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: white;
        }}
        .nav-links {{
            display: flex;
            gap: 20px; /* 메뉴 간격 조정 */
        }}
        .nav-links a, .nav-item {{
            color: white !important;
            text-decoration: none;
            font-weight: bold;
            padding: 10px 15px;
        }}
        .nav-item {{
            position: relative;
            cursor: pointer;
        }}
        /* 드롭다운 기본 상태 */
        .dropdown {{
            opacity: 0;               /* 처음엔 투명 */
            visibility: hidden;       /* 처음엔 보이지 않음 */
            position: absolute;
            top: 100%;
            left: 0;
            background-color: white;
            min-width: 220px;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
            padding: 10px;
            z-index: 10002;
            border-radius: 5px;
            transition: opacity 0.3s ease-in-out, visibility 0.3s ease-in-out; 
            /* 투명도와 visibility를 0.3초 동안 부드럽게 변경 */
        }}

        /* 드롭다운 아이템 스타일 */
        .dropdown a {{
            display: block;
            padding: 10px;
            text-decoration: none;
            color: black !important;
            font-weight: bold;
        }}
        .dropdown a:hover {{
            background-color: #f0a500;
            color: white;
        }}

        /* 마우스가 nav-item 또는 dropdown에 올라가 있을 때 */
        .nav-item:hover .dropdown,
        .dropdown:hover {{
            opacity: 1;            /* 투명도 1 (보이게) */
            visibility: visible;   /* 표시 */
        }}    
    </style>

    <div class="navbar">
        <div class="logo">LendingClub</div>
        <div class="nav-links">
            <span class="nav-item">대출
                <div class="dropdown">
                    <a href="/search_credit" target = "_self">간단한 금리 및 한도 조회</a>
                    <a href="/dashboard" target = "_self">시각화</a>
                </div>
            </span>
            <a href="/product" target = "_self">투자</a>
            <a href="/cs" target = "_self">고객상담</a>
            <a href="?login=true" class="nav-link">로그인</a>
        </div>
    </div>
""", unsafe_allow_html=True)

    
#------------로그인 폼 및 로그아웃 처리------------------#
# 로그인 창 표시 여부
if st.query_params.get("login") == "true":
    st.session_state.show_login = True

# 로그인 창 (모달 스타일)
if st.session_state.show_login and not st.session_state.logged_in:
    st.markdown("### 로그인")
    
    username = st.text_input("아이디:")
    password = st.text_input("비밀번호:", type="password")

    if st.button("로그인"):
        if username == "admin" and password == "1234":  # 예제용 간단한 로그인 검증
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.show_login = False
            st.success("로그인 성공! 회사 페이지로 이동합니다.")
            time.sleep(1)  # Give time for the success message to show
            st.experimental_set_query_params()  # Clear query parameters
            st.rerun()  # Rerun the app
            scriptrunner.StopException()
            st.switch_page("pages/company.py")



#-----------------------------------------페이지 구성 요소--------------------------------------------#
# --------------상단 섹션: 회사 정보 (회사명 & 슬로건)------------------#
# 상단 섹션 : 회사 정보 (회사명 & 슬로건)
st.markdown("""
    <div id="top" class="section top-bg">
        <h1>LendingClub</h1>
        <p>신뢰할 수 있는 금융 파트너, 더 나은 미래를 함께합니다.</p>
        <a href="loan_product" class="nav-link" style="background-color: #08298A; padding: 15px 30px; color: white; text-decoration: none; border-radius: 5px; font-size: 20px;">대출 상품 보기</a>

    </div>
""", unsafe_allow_html=True)

# --------------중단 섹션: 대출 상품 캐러셀------------------#
# UI 레이아웃
st.markdown('<div class="container">', unsafe_allow_html=True)

# 오른쪽 애니메이션 영역 (크기 조정 + 정렬 개선)
st.markdown('<div class="animation-container">', unsafe_allow_html=True)
if lottie_animation:
    st_lottie(lottie_animation, speed=1, height=350, key="investment_graph")  # 크기 조정 (height=350)
else:
    st.warning("애니메이션을 표시할 수 없습니다. JSON 파일을 확인하세요.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # 전체 컨테이너 닫기


# 오른쪽: 텍스트 설명
st.markdown('<div class="right-section">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">분산투자를 통한 안정적인 투자</div>
    <div class="subtitle">
        렌딧에서는 분산투자가 가능하여 <br>
        투자의 안정성과 수익성이 높아집니다.
    </div>
    """,
    unsafe_allow_html=True
)
# 버튼 추가
st.markdown(
    """
    <div class="button-container">
        <a href="invest" target="_self">
            <button class="button">투자 상품 보기</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)




# --------------하단 섹션: 회사 성장 데이터------------------#
# 제목
st.markdown("<br><br>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

st.markdown('<p class="big-font">렌딧의 현재</p>', unsafe_allow_html=True)

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

# 날짜 정보
st.markdown('<p class="footer">렌딧 내부 데이터 기준 (2025년 2월 23일)</p>', unsafe_allow_html=True)

# 버튼
st.markdown(
    """
    <div style="text-align: center;">
        <a href="search_credit" target="_blank">
            <button style="
                background-color: #4cc9a2;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 25px;
                cursor: pointer;
            ">1분만에 대출한도 알아보기</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True )


st.write("")
st.write("")
st.write("")

# 하단 화면 - 회사 소개 및 고객 지원
st.markdown('<p class="footer">고객센터: 1234-1234 | E-mail: support@LSB.co.kr</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">대표: 이수빈 | 사업자등록번호: 123-123-123</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">ⓒ PFC Technologies All rights reserved.</p>', unsafe_allow_html=True)
