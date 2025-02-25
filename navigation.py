import streamlit as st  

def load_navbar():
    st.markdown(f"""        
        <style>
            /* 네비게이션 바 스타일 */
            .navbar {{
                display: flex;
                justify-content: space-between; /* 로고와 메뉴 양쪽 정렬 */
                align-items: center;
                background-color:#1B262C;
                padding: 15px 30px;
            }}
            .logo {{
                font-size: 24px;
                font-weight: bold;
                color: white;
                font-family: "Alegreya", serif;
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
                background-color: #BDBDBD;
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
            <div class="logo">
                <a href="/" style="text-decoration: none; color: inherit;" target = "_self">
                LendSure
                </a>
            </div>
            <div class="nav-links">
                <span class="nav-item">대출
                    <div class="dropdown">
                        <a href="/search_credit" target = "_self">간단한 금리 및 한도 조회</a>
                        <a href="/loan_product" target = "_self">대출상품</a>
                        <a href="/dashboard" target = "_self">고객 인사이트 제공</a>
                    </div>
                </span>
                <a href="/invest" target = "_self">투자</a>
                <a href="/cs" target = "_self">고객상담</a>
                <a href="?login=true" class="nav-link">로그인</a>
            </div>
        </div>
        """, 
    unsafe_allow_html=True,
    ) 