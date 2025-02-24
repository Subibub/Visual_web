import streamlit as st
from navigation import load_navbar  # 공통 네비게이션 바 불러오기
from login_handler import init_login_state, handle_login, handle_logout # 로그인 처리 함수 불러오기
import time
import random
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="금리•한도조회-LendSure", layout="wide")

# 로그인 상태 초기화
init_login_state()

# 네비게이션 바 로드
load_navbar()  

# 로그인 / 로그아웃 처리
handle_login()
handle_logout()

# 현재 단계에 따라 스타일 동적 변경
step = st.session_state.get("step", 1)

def get_step_style(step_number):
    if step == step_number:
        return "background-color: #007bff; color: white; padding: 10px; border-radius: 5px;"
    return "background-color: #f8f9fa; color: black; padding: 10px; border-radius: 5px;"

# 네비게이션 바
st.markdown(
    f"""
    <style>
    .step-nav {{
        text-align: center;
        font-size: 18px;
        padding: 10px;
        border-bottom: 2px solid #ddd;
    }}
    .step-container {{
        display: flex;
        justify-content: center;
        gap: 20px;
    }}
    .step {{
        text-align: center;
        font-weight: bold;
    }}
    .content-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-top: 20px;
    }}
    </style>
    
    <div class="step-nav">
        <div class="step-container">
            <div class="step" style="{get_step_style(1)}">개인정보 입력 </div>
            <div class="step" style="{get_step_style(2)}">소득정보 입력 </div>
            <div class="step" style="{get_step_style(3)}">대출금액 입력</div>
            <div class="step" style="{get_step_style(4)}">결과 확인 </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# 중앙 정렬된 컨텐츠
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# 타이틀
st.title("대출 금리 및 한도 조회")
st.write("대출 가능성을 확인하고 맞춤 금리를 조회하세요.")

# Step 1: 개인정보 입력
if "step" not in st.session_state:
    st.session_state["step"] = 1

if st.session_state["step"] == 1:
    st.subheader("1️⃣ 개인정보 입력")
    name = st.text_input("이름", placeholder="이름을 입력하세요")
    age = st.number_input("나이", min_value=18,placeholder="나이를 입력하세요")
    phone = st.text_input("전화번호", placeholder="전화번호를 입력하세요")
    if st.button("다음 ➡️"):
        st.session_state["step"] = 2
        st.rerun()

# Step 2: 소득 정보 입력
elif st.session_state["step"] == 2:
    st.subheader("2️⃣ 소득 정보 입력")
    job_title = st.text_input("직업", placeholder="직업을 입력하세요")
    emp_length = st.selectbox("고용 기간", ["없음", "1년 미만", "1년 이상", "5년 이상", "10년 이상"])
    annual_inc = st.number_input("연간 소득(만원)", min_value=0, placeholder="연간 소득을 입력하세요")
    emp_type = st.selectbox("고용 형태", ["해당없음", "정규직", "계약직", "프리랜서"])
    other_inc = st.selectbox("기타 소득 유무", ["없음", "있음"])
    if other_inc == "있음":
        other_inc_amt = st.number_input("기타 소득(만원)", min_value=0, placeholder="기타 소득을 입력하세요")
    else:
        other_inc_amt = 0

    if st.button("다음 ➡️"):
        st.session_state["income"] = annual_inc
        st.session_state["other_income"] = other_inc_amt
        st.session_state["emp_length"] = emp_length
        st.session_state["emp_type"] = emp_type
        st.session_state["step"] = 3
        st.rerun()

# Step 3: 희망 대출 금액 입력
elif st.session_state["step"] == 3:
    st.subheader("3️⃣ 대출 금액 입력")
    loan_amount = st.number_input("희망 대출 금액 (만원)", min_value=0, placeholder="대출 금액을 입력하세요")
    loan_term = st.selectbox("대출 기간", ["12개월", "24개월", "36개월", "60개월"])
    if st.button("결과 확인"):
        st.session_state["step"] = 4
        st.rerun()

# Step 4: 결과 계산 및 표시
elif st.session_state["step"] == 4:
    st.subheader("4️⃣결과 확인")
    
    def calculate_loan_rate_and_limit(income, emp_length, emp_type):
        base_rate = 5.0  # 기본 금리
        loan_limit = income * 0.4  # 기본 대출 한도
        
        if emp_length == "10년 이상":
            base_rate -= 0.5
            loan_limit *= 1.2
        elif emp_length == "5년 이상":
            base_rate -= 0.3
            loan_limit *= 1.1
        elif emp_length == "1년 미만":
            base_rate += 0.5
            loan_limit *= 0.8
        
        if emp_type == "정규직":
            base_rate -= 0.2
            loan_limit *= 1.1
        elif emp_type == "계약직":
            base_rate += 0.3
            loan_limit *= 0.9
        elif emp_type == "프리랜서":
            base_rate += 0.5
            loan_limit *= 0.8
        
        return round(base_rate, 2), round(loan_limit, 2)
    
    total_income = st.session_state["income"] + st.session_state["other_income"]
    interest_rate, loan_amount = calculate_loan_rate_and_limit(total_income, st.session_state["emp_length"], st.session_state["emp_type"])
    
    st.write(f"✔️ 예상 대출 금리: **{interest_rate}%**")
    st.write(f"✔️ 예상 대출 한도: **${loan_amount:,} 만원**")
    st.success("이 정보는 참고용이며 실제 대출 심사 결과와 다를 수 있습니다.")
    
    if st.button("처음으로 돌아가기"):
        st.session_state["step"] = 1
        st.rerun()
    #상담받기 버튼 
    st.page_link("pages/cs.py", label = "상담받기", icon = "💬")

    
# 중앙 정렬된 컨텐츠 끝
st.markdown("</div>", unsafe_allow_html=True)

