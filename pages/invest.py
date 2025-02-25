import streamlit as st
from navigation import load_navbar  # 공통 네비게이션 바 불러오기
from login_handler import init_login_state, handle_login, handle_logout # 로그인 처리 함수 불러오기
import time
import pandas as pd
import requests
import json
from streamlit_lottie import st_lottie
import os
import numpy as np
import matplotlib.pyplot as plt



# 페이지 설정
st.set_page_config(page_title="투자상품-LendSure", layout="wide",page_icon="🛡️",initial_sidebar_state="collapsed")

# 로그인 상태 초기화
init_login_state()

# 네비게이션 바 로드
load_navbar()  

# 로그인 / 로그아웃 처리
handle_login()
handle_logout()

plt.rc('font', family='AppleGothic')  # MacOS




st.markdown(
    """
    <div style="background-color:#D0A9F5; padding: 100px; display: flex; align-items: center;">
        <div style="flex: 1;">
            <h2 >수익성과 안정성을 모두 고려한 투자</h2>
            <p>데이터로 입증된 투자,렌드슈어와 함께 수익성과 안정성을 극대화하세요!</p>
        </div>
        <div style="flex: 1; text-align: right;">
            <img src="https://cdn-icons-png.flaticon.com/512/2331/2331941.png" alt="People Icon" width="250"/>
        </div>
    </div>
    """,
        unsafe_allow_html=True
    )
st.markdown("<br>", unsafe_allow_html=True)



# 상품 데이터 업데이트

# 투자 상품 데이터 예시 (CSV, JSON 활용 가능)
df = {
    "상품명": ["아파트", "아파트","아파트", "증권", "신용"],
    "연 수익률": ["11.4", "14.5%", "8.5%", "8.5%", "14.9"],
    "유효담보비율": ["52.33%", "60.83%","24.30%", "-", "-"],
    "투자기간": ["12개월", "12개월", "12개월", "3개월", "48개월"],
    "모집금액": ["6000만 원", "2000만 원", "5000만 원","3000만원", "3000만 원"]
}

df = pd.DataFrame(df)

# 상품별 아이콘 URL 매칭 (튜플 리스트)
icon_urls = {
    "아파트": "https://img.icons8.com/ios-filled/50/4A90E2/home.png", 
    "증권": "https://img.icons8.com/ios-filled/50/4A90E2/line-chart.png",
    "신용": "https://img.icons8.com/ios-filled/50/4A90E2/bank-card-back-side.png",
    }

# 스타일 설정 (가로 2개씩 배치)
st.markdown("""
    <style>
        .product-grid { 
            display: flex; 
            flex-wrap: wrap; 
            gap: 20px; 
            justify-content: center; 
        }
        .product-card {
            width: 45%; 
            min-width: 300px; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 20px; 
            margin: 10px; 
            background-color: white; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            text-align: center; 
            font-family: 'Arial', sans-serif;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .product-card h3 {
            color: #071952;
        }
        .icon {
            width: 50px;
            height: 50px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)


# 상품 정보 출력
rows = [df.iloc[i:i+2] for i in range(0, len(df), 2)]  # 2개씩 묶어서 행 생성

for row in rows:
    cols = st.columns(2)  # 한 줄에 2개 배치
    for i, (idx, item) in enumerate(row.iterrows()):
        with cols[i]:
            st.markdown(
                f"""    
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin: 10px; 
                            background-color: white; text-align: center; 
                            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                            font-family: Arial, sans-serif;">                    
                    <img src="{icon_urls[item["상품명"]]}" alt="Invest Icon"/>
                    <h3 style="color: #0719522;">{item["상품명"]}</h3>
                    <p><strong>연 수익률:</strong> {item["연 수익률"]}</p>
                    <p><strong>유효담보비율:</strong> {item["유효담보비율"]}</p>
                    <p><strong>투자기간:</strong> {item["투자기간"]}</p>
                    <p><strong>모집금액:</strong> {item["모집금액"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

#데이터 가공 
df["연 수익률"] = df["연 수익률"].str.replace('%', '', regex=False).astype(float)
df["유효담보비율"] = pd.to_numeric(df["유효담보비율"].str.replace('%', '', regex=False), errors='coerce')
df["유효담보비율"] = df["유효담보비율"].astype(float)


# 수익 시뮬레이션
with st.expander("✖️수익 계산기✖️"):
    st.subheader("수익 시뮬레이션")
    invest_amt = st.number_input("투자 금액 (만원)", min_value=10, max_value=10000, value=1000)
    annual_return= st.slider("예상 연 수익률 (%)", min_value=5.0, max_value=20.0, value=10.0, step=0.1)
    invest_term = st.slider("투자 기간 (년)", min_value=1, max_value=10, value=3)
    tax = st.checkbox("세금 적용 (15% 세금 공제)")

    # 수익 계산
    total_revenue = invest_amt * ((1 + annual_return / 100) ** invest_term)
    after_tax_rev = total_revenue * 0.85 if tax else total_revenue

    st.write(f"투자 후 예상 총 수익: {total_revenue:.2f} 만원")
    if tax:
        st.write(f" 세금 적용 후 수익: {after_tax_rev:.2f} 만원")

    # 수익 그래프
    fig2, ax2 = plt.subplots()
    years = np.arange(1, invest_term + 1)
    profits = [invest_amt * ((1 + annual_return / 100) ** year) for year in years]
    ax2.plot(years, profits, marker='o', linestyle='-')
    ax2.set_xlabel("투자 기간 (년)")
    ax2.set_ylabel("예상 수익 (만원)")
    ax2.set_title("연도별 예상 수익 증가")
    st.pyplot(fig2)

