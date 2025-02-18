import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="금리•한도조회")

# 🎯 신용 점수 안내 페이지
st.title("❓ 신용 점수 추정 방법")
st.write("""
신용 점수를 모를 경우 다음 방법을 참고하세요:
1. 은행 또는 금융기관에서 신용 보고서 요청하기
2. 신용 점수 무료 조회 서비스 이용하기
3. 기존 대출 또는 신용카드 사용 내역 확인하기
""")

# 금리 ,한도 조회하기
st.subheader("간편하게 금리•한도 조회하기 ")
st.write("""
정확한 금리와 한도가 아닙니다. 대출을 원하시면 상담 요청하셔서 
더 정확한 정보를 확인하세요.

신용 점수가 낮거나 없어도 대출 가능한 경우가 있습니다.
대출 가능성을 높이기 위해 다음 사항을 고려하세요:
- 소득 및 고용 기록 확인
- 부동산 또는 자동차 담보 제공
- 공동 신청자 추가
""")

# 개인정보 입력
st.subheader("📝 개인정보 입력")
name = st.text_input("이름")
age = st.number_input("나이", min_value=0)
phone = st.text_input("전화번호")

# 소득 정보
job_title = st.text_input("직업")
emp_length = st.selectbox("고용 기간", ["없음", "1년 미만", "1년 이상", "5년 이상", "10년 이상"])
annual_inc = st.number_input("연간 소득(USD)", min_value=0, format="%d")
emp_type = st.selectbox("고용 형태", ["해당없음", "정규직", "계약직", "프리랜서"])

# 기타 소득 유무
other_inc = st.selectbox("기타 소득 유무", ["없음", "있음"])
if other_inc == "있음":
    other_inc_amt = st.number_input("기타 소득(USD)", min_value=0, format="%d")

# 집 소유 여부
home_ownership = st.selectbox("집 소유 여부", ["무", "유"])

# 결혼 및 부양가족 여부
marital_status = st.selectbox("결혼 여부", ["미혼", "기혼", "이혼"])
depend_number = st.selectbox("부양 가족 수", ["0명", "1명", "2명", "3명 이상"])

# 신용정보 입력
fico_score = st.number_input("FICO 신용 점수", min_value=300, max_value=850, format="%d")
rest_loan = st.number_input("기존 대출 잔액(USD)", min_value=0, format="%d")
dti = st.number_input("부채 비율(DTI, %)", min_value=0.0, format="%f")
delinq_2yrs = st.number_input("최근 2년 연체 횟수", min_value=0, format="%d")

# 대출정보 입력
st.subheader("📝 대출 정보 입력")
purpose = st.selectbox("대출 목적", ["신용카드 상환", "부동산 구매", "차량 구매", "기타"])
loan_amt = st.number_input("희망 대출 금액(USD)", min_value=0, format="%d")
loan_term = st.number_input("희망 대출 기간(개월)", min_value=1, format="%d")

# ------------------------------------------------
# 📌 예상 금리 & 한도 계산 함수
def calculate_interest_rate(fico_score, dti):
    """ 신용 점수와 부채 비율(DTI)을 기반으로 예상 금리 계산 """
    if fico_score >= 750:
        base_rate = 3.5
    elif fico_score >= 700:
        base_rate = 5.0
    elif fico_score >= 650:
        base_rate = 7.0
    else:
        base_rate = 10.0
    
    # DTI(부채 비율)가 높으면 금리 가산
    rate_adjustment = min(dti * 0.1, 5)  # 최대 5% 증가
    return round(base_rate + rate_adjustment, 2)

def calculate_loan_limit(annual_inc, dti):
    """ 연소득과 부채 비율을 기반으로 대출 가능 한도 계산 """
    max_limit = annual_inc * 0.4  # 연소득의 40%를 대출 한도로 설정
    dti_adjustment = max_limit * (1 - dti / 100)  # 부채 비율에 따라 조정
    return round(max(dti_adjustment, 5000))  # 최소 한도는 $5000

# 📌 버튼 클릭 시 예상 금리 & 한도 팝업
if st.button("📊 대출 금리 확인"):
    if fico_score and dti and annual_inc:
        # 금리 & 한도 계산
        estimated_rate = calculate_interest_rate(fico_score, dti)
        estimated_limit = calculate_loan_limit(annual_inc, dti)

        # 팝업 창 띄우기
        with st.expander("📢 예상 대출 조건 확인"):
            st.success(f"💰 예상 금리: **{estimated_rate}%**")
            st.success(f"💳 예상 대출 한도: **${estimated_limit:,}**")
            st.write("이 정보는 예상 값이며, 실제 대출 조건은 다를 수 있습니다.")
            st.write("---")
            st.write("📊 **대출 시각화 보기** 버튼을 눌러 더 자세한 분석을 확인하세요!")

        # 대시보드 페이지로 이동 버튼
        if st.button("📊 대출 시각화 보기"):
            st.session_state["redirect_to_dashboard"] = True

#대시보드 페이지로 자동 이동
if "redirect_to_dashboard" in st.session_state and st.session_state["redirect_to_dashboard"]:
    st.session_state["redirect_to_dashboard"] = False  # 상태 초기화
    st.switch_page("dashboard")  # `pages/dashboard.py`로 이동

# 🔙 홈으로 돌아가기 버튼
if st.button("🔙 홈으로 돌아가기"):
    st.switch_page("app.py")  # 홈으로 이동