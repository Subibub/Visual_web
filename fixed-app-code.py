import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title='렌딧', layout='wide')

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
            <a href="#">고객상담</a>
            <a href="?login=true" class="nav-link">로그인</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 스타일 적용
st.markdown(
    """
    <style>
        .main-container {
            background: linear-gradient(135deg, #4CAF50, #2E7D32);
            padding: 60px;
            border-radius: 15px;
            text-align: center;
            color: white;
        }
        .main-title {
            font-size: 36px; font-weight: bold;
        }
        .sub-title {
            font-size: 24px;
        }
        .button-container {
            margin-top: 20px;
        }
        .metric-container {
            display: flex; justify-content: space-around; margin-top: 40px;
        }
        .footer {
            text-align: center; margin-top: 60px; font-size: 14px; color: #666666;
        }
        .custom-button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: white;
            color: #2E7D32;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    """ 
    , unsafe_allow_html=True
)

# 첫 화면 - 배경 포함
st.markdown(
    '<div class="main-container">' 
        '<p class="main-title">Lending Club</p>' 
        '<p class="sub-title">더 나은 대출과 투자의 시작</p>' 
        '<div class="button-container">' 
            '<button class="custom-button">자세히 보기</button>' 
        '</div>' 
    '</div>',
    unsafe_allow_html=True
)


# 중간 화면 - 주요 금융 정보
st.markdown("### 주요 금융 정보")
st.markdown('<div class="metric-container">', unsafe_allow_html=True)
st.metric(label="평균 수익률", value="10.85%", delta="0.001")
st.metric(label="누적 투자 건수", value="2,927,911건", delta="-45,765")
st.metric(label="평균 누적 투자금액", value="426만원", delta="-38")
st.metric(label="재투자율", value="54.77%")
st.markdown('</div>', unsafe_allow_html=True)





# 하단 화면 - 회사 소개 및 고객 지원
st.markdown("### 회사소개 및 고객 지원")
st.markdown('<p class="footer">고객센터: 1600-9613 | E-mail: support@cple.co.kr</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">대표: 이수환 | 사업자등록번호: 668-88-00027</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">ⓒ PFC Technologies All rights reserved.</p>', unsafe_allow_html=True)
