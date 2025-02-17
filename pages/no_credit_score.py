import streamlit as st

# 페이지 설정
st.set_page_config(page_title="신용 점수 안내", page_icon="❓")

# 🎯 신용 점수 안내 페이지
st.title("❓ 신용 점수 추정 방법")
st.write("""
신용 점수를 모를 경우 다음 방법을 참고하세요:
1. 은행 또는 금융기관에서 신용 보고서 요청하기
2. 신용 점수 무료 조회 서비스 이용하기
3. 기존 대출 또는 신용카드 사용 내역 확인하기
""")

#대출가능성 파악하기 
st.subheader("대출 가능성 파악하기")
st.write("""
신용 점수가 낮거나 없어도 대출 가능한 경우가 있습니다.
대출 가능성을 높이기 위해 다음 사항을 고려하세요:
- 소득 및 고용 기록 확인
- 부동산 또는 자동차 담보 제공
- 공동 신청자 추가
""")
# 개인정보 입력받기 
st.subheader("📝 개인정보 입력")
#이름,나이,전화번호
name = st.text_input("이름")
age = st.number_input("나이", min_value=0)
phone = st.number_input("전화번호", format="%d")
#소득정보 
job_title = st.text_input("직업")
emp_length = st.selectbox("고용 기간", ["없음","1년 미만", "1년 이상", "5년 이상", "10년 이상"])
annual_inc = st.number_input("연간 소득(USD)", min_value=0, format="%d")
emp_type = st.selectbox("고용 형태", ["해당없음","정규직", "계약직", "프리랜서"])

#다른 소득 유무 
other_inc = st.selectbox("기타 소득 유무", ["없음", "있음"])
#다른 소득 있으면 입력
if other_inc == "있음":
    other_inc_amt = st.number_input("기타 소득(USD)", min_value=0, format="%d")
#집소유 유무 
home_ownership = st.selectbox("집 소유 여부", ["무", "유"])

#결혼 및 부양가족 여부 
marital_status = st.selectbox("결혼 여부", ["미혼", "기혼", "이혼"])
depend_number= st.selectbox("부양 가족 수", ["0명", "1명", "2명", "3명 이상"])

#신용정보 입력받기 
fico_score = st.number_input("FICO 신용 점수", min_value=300, max_value=850, format="%d")
rest_loan = st.number_input("기존 대출 잔액(USD)", min_value=0, format="%d")
dti = st.number_input("부채 비율(DTI, %)", min_value=0.0, format="%f")
delinq_2yrs = st.number_input("최근 2년 연체 횟수", min_value=0, format="%d")

#대출정보 입력받기
st.subheader("📝 대출 정보 입력")
puropose = st.selectbox("대출 목적", ["신용카드 상환", "부동산 구매", "차량 구매", "기타"])
loan_amt = st.number_input("희망 대출 금액(USD)", min_value=0, format="%d")
loan_term = st.number_input("희망 대출 기간(개월)", min_value=1, format="%d")



#------------------------------------------------
# 🔙 홈으로 돌아가는 버튼
if st.button("🔙 홈으로 돌아가기"):
    st.switch_page("app.py")  # ✅ 홈으로 이동