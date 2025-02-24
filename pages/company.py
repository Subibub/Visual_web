import streamlit as st

st.set_page_config(page_title="대출 상담 분석 대시보드-LendSure", layout="wide")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os 
from navigation import load_navbar
from login_handler import init_login_state


init_login_state()  # 세션 상태 초기화

# 네비게이션 바 표시
load_navbar()

if st.session_state["logged_in"]:
    st.title(f"admin님, 환영합니다!")
else:
    st.title("환영합니다! 로그인해 주세요.")

#=====================================================================================
# Streamlit 멀티페이지 설정
st.sidebar.title("📌 페이지 선택")
page = st.sidebar.radio("이동할 페이지를 선택하세요", ["대출 개요", "대출 분석", "고객 세부 정보", "기타 분석"])

# 데이터 로드 함수
def load_data():
    file_path = "/Users/isubin/VW/data/data_preprocessed_v4.csv"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}. Check the path and try again.")
    
    return pd.read_csv(file_path)

# 데이터 로드
@st.cache_data
def get_data():
    return load_data()
df = get_data()


#==================================================================================================
#세부 페이지 

if page == "대출 개요":
    st.title(" 대출 상담 고객 데이터 개요")
    st.write("대출 상담 고객 데이터의 기본 통계를 확인할 수 있습니다.")
    st.dataframe(df.describe())

     # 대출 금액 vs 신용 점수 밀도 히트맵
    st.subheader("대출 금액 vs 신용 점수 밀도 히트맵")
    fig_heatmap = px.density_heatmap(
        df, 
        x="loan_amnt", 
        y="fico_avg", 
        marginal_x="rug", 
        marginal_y="histogram",
        title="대출 금액과 신용 점수의 밀도 분포",
        color_continuous_scale=["#e0f2e9", "#74c69d", "#40916c", "#1b4332"]  # 연한 초록 → 진한 초록
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

elif page == "대출 분석":
    st.title(" 대출 데이터 분석")
    
    # 사이드바 필터 설정
    st.sidebar.header("🔍 데이터 필터링")
    selected_term = st.sidebar.selectbox("대출 기간 선택 (개월)", df["term"].unique())
    selected_grade = st.sidebar.multiselect("신용 등급 선택", sorted(df["grade"].unique()))
    filtered_df = df[(df["term"] == selected_term)]
    if selected_grade:
        filtered_df = filtered_df[filtered_df["grade"].isin(selected_grade)]

    # 1. 대출 금액 분포 시각화
    st.subheader("대출 금액 분포")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(filtered_df["loan_amnt"], bins=30, kde=True, ax=ax,color='green')
    ax.set_xlabel("대출 금액 ($)")
    ax.set_ylabel("빈도")
    ax.set_title("대출 금액 분포")
    st.pyplot(fig)

    # 2. 신용 등급별 대출 현황
    st.subheader("신용 등급별 대출 현황")
    grade_counts = filtered_df["grade"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=grade_counts.index, y=grade_counts.values, ax=ax, palette="Greens")
    ax.set_xlabel("신용 등급")
    ax.set_ylabel("대출 건수")
    ax.set_title("신용 등급별 대출 현황")
    st.pyplot(fig)

elif page == "고객 세부 정보":
    st.title("고객 세부 정보 분석")
    
    # 고객 개별 분석 (번호로 검색하도록 변경)
    st.sidebar.header("고객 선택")
    customer_id = st.sidebar.number_input("고객 ID 입력", min_value=0, max_value=len(df) - 1, step=1)
    customer_data = df.iloc[customer_id]
    
    # 고객 정보 표
    st.write("### 고객 상세 정보")
    st.dataframe(pd.DataFrame(customer_data).T)
    
    # 대출 상태 시각화 (산점도로 변경, 0과 1만 표시 + 선택 고객 강조)
    st.subheader("대출 상태 산점도")
    df_filtered = df[df["loan_status"].isin([0, 1])]  # 0과 1만 필터링
    
    fig = px.scatter(df_filtered, x="loan_amnt", y="fico_avg", color="loan_status", 
                     title="대출 금액 vs 신용 점수 (대출 상태별)",
                     labels={"loan_amnt": "대출 금액 ($)", "fico_avg": "신용 점수", "loan_status": "대출 상태"},
                     size_max=10, opacity=0.7,
                     color_discrete_sequence=["green"]  # ✅ 연한 초록 -> 중간 초록 -> 진한 초록

                     )
    
    # 선택된 고객 강조
    fig.add_scatter(x=[customer_data["loan_amnt"]], y=[customer_data["fico_avg"]],
                    mode="markers", marker=dict(size=20, color="red", symbol="star"))
    
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    
    # 1번 페이지와의 비교 시각화
    st.subheader("📊 고객 데이터 vs 전체 데이터 비교")
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # 고객의 대출 금액과 전체 데이터 비교
    sns.histplot(df["loan_amnt"], bins=30, kde=True, ax=axes[0], color='green', label="전체 데이터")
    axes[0].axvline(customer_data["loan_amnt"], color='red', linestyle='dashed', linewidth=2)
    axes[0].set_title("대출 금액 비교")
    
    # 고객의 신용 점수와 전체 데이터 비교
    sns.histplot(df["fico_avg"], bins=30, kde=True, ax=axes[1], color='green', label="전체 데이터")
    axes[1].axvline(customer_data["fico_avg"], color='red', linestyle='dashed', linewidth=2)
    axes[1].set_title("신용 점수 비교")
    
    st.pyplot(fig)

if page == "기타 분석":
    st.title("기타 분석")
    st.write("이 페이지에서는 연도별 대출 데이터를 분석합니다.")
    
    # 연도별 대출 분포 (밀도 컨투어)
    st.subheader(" 연도별 대출 분포 (Density Contour)")
    
    if "term" in df.columns:
        if df["term"].dtype == object:  # 문자열이면 변환
            df["term_numeric"] = df["term"].str.extract(r'(\d+)').astype(float)
        elif df["term"].dtype in [int, float]:  # 숫자이면 바로 사용
            df["term_numeric"] = df["term"]
        
        df["estimated_issue_year"] = 2025 - (df["term_numeric"] / 12)  # 대출 기간을 기준으로 발생 연도 추정
        
        fig_contour = px.density_contour(df, x="loan_amnt", y="fico_avg", color="estimated_issue_year", title="연도별 대출 금액 분포 (각 등고선 = 동일 연도)")
        
        st.plotly_chart(fig_contour, use_container_width=True)
    else:
        st.warning("⚠️ 대출 발생 연도를 추정할 수 있는 컬럼이 없습니다. 'term' 컬럼을 확인해주세요.")