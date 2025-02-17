import streamlit as st

# 페이지 설정
st.set_page_config(page_title="LendingClub Dashboard", page_icon="💰")

# 🎯 홈 페이지 - 회사 소개 및 이동 버튼
st.title("💰 LendingClub 대출 서비스")
st.write("LendingClub은 대출 신청자에게 최적의 대출 조건을 제공합니다.")

col1, col2 = st.columns(2)

with col1:
    if st.button("📊 대출 데이터 시각화 보기"):
        st.switch_page("pages/dashboard.py")  # ✅ 대시보드 페이지 이동

with col2:
    if st.button("❓ 신용 점수를 모르는 경우"):
        st.switch_page("pages/no_credit_score.py")  # ✅ 신용 점수 안내 페이지 이동