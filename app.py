import streamlit as st
import sqlite3

# 페이지 기본 설정
st.set_page_config(page_title="LendingClub", layout="wide")

#  세션 상태 초기화 (로그인 관리)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# CSS 로 맨 위 검은색 네비게이션 바 추가 
st.markdown("""
    <style>
        .top-bar {
            background-color: #000000; /* 검은색 배경 */
            height: 60px;
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 9999;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 40px;
            box-shadow: 0px 2px 10px rgba(255, 255, 255, 0.1);
        }
        .top-bar div {
            display: flex;
            align-items: center;
            gap: 20px;
        }
        .top-bar button {
            background: none;
            color: white;
            border: 1px solid white;
            font-size: 16px;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
            transition: background 0.3s ease-in-out, color 0.3s;
        }
        .top-bar button:hover {
            background: white;
            color: black;
        }
        .content {
            margin-top: 80px;  /* 네비게이션 바가 가리지 않도록 추가 여백 */
        }
    </style>
    <div class="top-bar">
        <div>
            <span style="color: white; font-size: 20px; font-weight: bold;">LendingClub</span>
        </div>
        <div>
            <button onclick="window.location.href='/loan'">📌 대출 신청</button>
            <button onclick="window.location.href='/invest'">💰 투자 신청</button>
        </div>
        <div>
            <button onclick="window.location.href='/settings'">⚙️ 설정</button>
        </div>
    </div>
    <div class="content"></div>  <!-- 본문 내용의 여백 추가 -->
""", unsafe_allow_html=True)

# JavaScript (Streamlit 내부에서 페이지 이동)
st.markdown("""
    <script>
        function switch_to_loan() {
            window.location.href = '/pages/loan.py';
        }
        function switch_to_invest() {
            window.location.href = '/pages/invest.py';
        }
        function open_sidebar() {
            window.dispatchEvent(new Event("open-sidebar"));
        }
    </script>
""", unsafe_allow_html=True)

# 여백 추가 (네비게이션 바가 고정되므로 내용이 가려지지 않도록)
st.write("")
st.write("")
st.write("")

#  로그인 버튼 클릭 시, 사이드바에서 로그인 창 표시
with st.sidebar:
    st.markdown("### ⚙️ 설정")
    if not st.session_state.logged_in:
        with st.expander("🔐 로그인"):
            username = st.text_input("아이디")
            password = st.text_input("비밀번호", type="password")

            if st.button("로그인"):
                if username == "admin" and password == "1234":  # 🎯 테스트 계정
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("✅ 로그인 성공! 회사 웹페이지로 이동합니다.")
                    st.switch_page("pages/company.py")  # ✅ 회사 직원 페이지 이동
                else:
                    st.error("❌ 아이디 또는 비밀번호가 잘못되었습니다.")
    else:
        st.write(f"👤 **{st.session_state.username}** 님 환영합니다!")
        if st.button("🚪 로그아웃"):
            st.session_state.logged_in = False
            st.experimental_rerun()


# 상단: 회사 정보 (회사명 & 슬로건)
with st.container():
    st.markdown("""
        <style>
            .title {
                text-align: center;
                font-size: 48px;
                font-weight: bold;
                color: #333;
                margin-bottom: 5px;
            }
            .slogan {
                text-align: center;
                font-size: 20px;
                color: #666;
                margin-bottom: 30px;
            }
        </style>
        <div class='title'>LendingClub</div>
        <div class='slogan'>"신뢰할 수 있는 금융 파트너, 더 나은 미래를 함께합니다."</div>
    """, unsafe_allow_html=True)





# 중단: 상품 캐러셀 (좌우로 이동 가능하게)
st.markdown("<h2 style='text-align: center;'> 인기 대출 상품</h2>", unsafe_allow_html=True)

# 데이터베이스에서 대출 상품 가져오기
def get_loan_products():
    conn = sqlite3.connect("data/products.db")  # 데이터베이스 연결
    cursor = conn.cursor()
    cursor.execute("SELECT name, rate, description, image_url FROM loan_products")
    products = cursor.fetchall()
    conn.close()
    return products

products = get_loan_products()

# 세션 상태 초기화 (캐러셀 인덱스 관리)
if "carousel_index" not in st.session_state:
    st.session_state.carousel_index = 0

# 캐러셀 이동 함수
def move_carousel(direction):
    if direction == "prev":
        st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(products)
    elif direction == "next":
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(products)

# 중단: 상품 캐러셀 (◀️ / ▶️ 버튼으로 이동 가능)

if products:
    index = st.session_state.carousel_index  # 현재 인덱스 가져오기
    name, rate, description, image_url = products[index]

    # 캐러셀 UI
    with st.container():
        col1, col2, col3 = st.columns([1, 4, 1])  # ◀️ 버튼 / 상품 정보 / ▶️ 버튼

        with col1:
            if st.button("<", key="prev_btn"):
                move_carousel("prev")  # 이전 상품

        with col2:
            st.image(image_url, width=250)
            st.markdown(f"<h3 style='text-align:center;'> {name}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'> <b>금리:</b> {rate}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'>  {description}</p>", unsafe_allow_html=True)

        with col3:
            if st.button(">", key="next_btn"):
                move_carousel("next")  # 다음 상품

st.write("---")  # 구분선 추가

# 하단: 회사 성장 데이터
st.markdown("<h2 style='text-align: center;'> 현재 모습 </h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="📊 누적 투자액", value="$1.2B", delta="+10% MoM")

    with col2:
        st.metric(label="👤 평균 인당 투자 금액", value="$12,500", delta="+5% MoM")

    with col3:
        st.metric(label="💰 승인된 대출 건수", value="250,000", delta="+8% MoM")