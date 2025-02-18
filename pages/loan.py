import streamlit as st

# 페이지 설정
st.set_page_config(page_title="대출 신청", layout="wide")

# 상단 네비게이션 바
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.markdown("### 💰 LendingClub")  # 회사 로고
with col2:
    pass  # 중간 공간 확보
with col3:
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("📌 대출 신청"):
            st.switch_page("pages/loan.py")  # 현재 페이지
    with col_btn2:
        if st.button("💰 투자하기"):
            st.switch_page("pages/invest.py")  # 투자 페이지 이동

st.write("---")

# 📌 대출 한도 및 금리 조회
st.markdown("## 📌 대출 한도 및 금리 조회")
st.write("대출 한도와 금리를 빠르게 확인하고, 맞춤형 대출 옵션을 찾아보세요.")

# 🔵 대출 조회 카드 스타일
with st.container():
    st.markdown("""
        <style>
            .loan-card {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="loan-card">📊 대출 금리와 한도를 확인하세요!</div>', unsafe_allow_html=True)

    st.write("")
    
    # 🎯 버튼 추가 (기존 no_credit_score.py 페이지로 연결)
    if st.button("💳 금리, 한도 조회하기"):
        st.switch_page("pages/no_credit_score.py")  # 신용 점수 없이 조회 페이지로 이동