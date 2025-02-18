import streamlit as st
import time

# 페이지 기본 설정
st.set_page_config(page_title="LendingClub", layout="wide")

# 🌟 세션 상태 초기화 (로그인 관리)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# 🔧 상단 네비게이션 바
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.markdown("### 💰 LendingClub")  # 회사 로고
with col2:
    pass  # 중간 공간 확보
with col3:
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("📌 대출 신청"):
            st.switch_page("pages/loan.py")  # 대출 페이지 이동
    with col_btn2:
        if st.button("💰 투자하기"):
            st.switch_page("pages/invest.py")  # 투자 페이지 이동

st.write("---")

# 🔧 상단 우측 설정 아이콘 (로그인 관리)
with st.sidebar:
    st.markdown("### ⚙️ 설정")

    # ✅ 로그인 페이지
    if not st.session_state.logged_in:
        with st.expander("🔐 로그인"):
            username = st.text_input("아이디", key="username")
            password = st.text_input("비밀번호", type="password", key="password", help="테스트 계정: admin / 1234")

            if st.button("로그인"):
                # 🎯 [테스트 계정] 아이디 & 비밀번호 검증
                if username == "admin" and password == "1234":  
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"✅ 로그인 성공! {username} 님, 회사 웹페이지로 이동합니다.")
                    time.sleep(1)  # 1초 대기 후 페이지 이동
                    st.switch_page("pages/company.py")  # 내부 직원용 페이지로 이동
                else:
                    st.error("❌ 아이디 또는 비밀번호가 잘못되었습니다.")

    # ✅ 로그인 성공 시, 유저 정보 표시 및 로그아웃 버튼
    else:
        st.write(f"👤 **{st.session_state.username}** 님 환영합니다!")
        if st.button("🚪 로그아웃"):
            # 세션 상태 초기화 후 페이지 새로고침
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()

st.write("---")

# 🔥 움직이는 상품 목록 (캐러셀)
st.markdown("### 🔥 인기 대출 상품")

products = [
    {
        "name": "개인 신용 대출",
        "rate": "연 4.5%",
        "desc": "신용 등급에 따라 차등 적용",
        "img": "https://source.unsplash.com/300x200/?money,finance"
    },
    {
        "name": "소상공인 대출",
        "rate": "연 3.8%",
        "desc": "사업 운영자를 위한 맞춤 대출",
        "img": "https://source.unsplash.com/300x200/?business,loan"
    },
    {
        "name": "주택 담보 대출",
        "rate": "연 2.9%",
        "desc": "부동산 담보 제공 시 가능",
        "img": "https://source.unsplash.com/300x200/?house,mortgage"
    },
    {
        "name": "자동차 대출",
        "rate": "연 5.2%",
        "desc": "신차 및 중고차 구입 시",
        "img": "https://source.unsplash.com/300x200/?car,loan"
    },
]

product_placeholder = st.empty()  # 빈 공간 생성

for _ in range(10):  # 자동 슬라이드 효과
    for product in products:
        with product_placeholder.container():
            col_img, col_text = st.columns([1, 2])  # 이미지와 텍스트 나누기

            with col_img:
                st.image(product["img"], width=200)

            with col_text:
                st.subheader(f"🚀 {product['name']}")
                st.write(f"💲 **금리:** {product['rate']}")
                st.write(f"ℹ️ {product['desc']}")

            st.write("---")
        time.sleep(2)  # 2초마다 변경