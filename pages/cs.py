import streamlit as st

st.set_page_config(page_title="고객센터", page_icon="📞", layout="wide")


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


# 스타일 커스텀: 폰트, 버튼, 레이아웃 개선
st.markdown(
    """
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
        }
        .sub-navbar {
            text-align: center;
            font-size: 18px;
            padding: 10px;
            border-bottom: 2px solid #ddd;
        }
        .contact-box {
            background: rgba(52, 152, 219, 0.9);
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 18px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
    
        }
        .custom-button {
            display: inline-block;
            padding: 15px 30px;
            font-size: 18px;
            color: white !important; 
            background-color: #088A68;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            transition: 0.3s;
            text-align: center;
            width: 220px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
        .custom-button:hover {
            background-color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='sub-navbar'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='contact-box'>
    <p><h1>고객센터 운영 시간</h1></p>
    <p>상담시간: 평일 9시 - 18시 (주말, 공휴일, 대체휴일 제외)</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

st.markdown("""
<div class="button-container">
    <a href="tel:18334235" class="custom-button">📞 대출 상담하기 (1833-4235)</a>
    <a href="tel:18335073" class="custom-button">📞 투자 상담하기 (1833-5073)</a>
</div>
""", unsafe_allow_html=True)