import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt

# 페이지 설정
st.set_page_config(page_title="대출 데이터 대시보드", page_icon="📊")

# 데이터 로드 함수
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/lendingclub_data.csv")  # 데이터 폴더에서 로드
    except FileNotFoundError:
        df = pd.DataFrame({
            "annual_inc": [50000, 60000, 70000, 80000, 90000],
            "fico_range_low": [650, 700, 750, 800, 850],
            "loan_amnt": [5000, 10000, 15000, 20000, 25000],
            "int_rate": [7.5, 8.0, 9.0, 10.5, 12.0],
            "delinq_2yrs": [0, 1, 0, 2, 1],
            "addr_state": ["CA", "TX", "NY", "FL", "WA"]
        })
    return df

df = load_data()

# 🎯 대시보드 페이지
st.title("📊 LendingClub 데이터 시각화")

# 📌 금융 지표 요약
st.subheader("📈 주요 금융 지표")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📉 평균 이자율", f"{df['int_rate'].mean():.2f}%")
with col2:
    st.metric("💰 평균 대출 금액", f"${df['loan_amnt'].mean():,.0f}")
with col3:
    st.metric("⚠️ 평균 연체율", f"{df['delinq_2yrs'].mean():.2f} 건")
#-------------------------------------------
# 1. 대출 상태(Loan Status) & 신용 점수 vs 이자율
st.subheader("📊 대출 상태별 분포 & 신용 점수 vs 이자율")
col1, col2, col3 = st.columns([1, 1, 1])  # 3개 컬럼 배치

fig1 = px.pie(df, names="loan_status", title="대출 상태별 대출 비율", width=400, height=400)
col1.plotly_chart(fig1)

fig2 = px.scatter(df, x="fico_avg", y="int_rate", color="loan_amnt",
                  title=" 신용 점수 vs 이자율",
                  labels={"fico_avg": "신용 점수", "int_rate": "이자율 (%)"},
                  width=400, height=400)
col2.plotly_chart(fig2)

avg_values = df.groupby("grade").agg({"loan_amnt": "mean", "int_rate": "mean"}).reset_index()
fig3 = px.bar(avg_values, x="grade", y=["loan_amnt", "int_rate"], barmode="group",
              title="등급별 평균 대출 금액 & 평균 이자율",
              width=400, height=400)
col3.plotly_chart(fig3)

# 2.대출 목적(Treemap) & 주택 소유별 대출 금액
st.subheader("📊 대출 목적 및 주택 소유별 대출 금액")
col4, col5 = st.columns([1.5, 1])  # 첫 번째 컬럼을 더 넓게 설정

fig4 = px.treemap(df, path=["purpose"], values="loan_amnt",
                  title="대출 목적별 대출 금액 분포",
                  width=600, height=450)
col4.plotly_chart(fig4)

avg_home_loan = df.groupby("home_ownership")["loan_amnt"].mean().reset_index()
fig5 = px.bar(avg_home_loan, x="home_ownership", y="loan_amnt",
              title="주택 소유별 평균 대출 금액",
              color="home_ownership",
              width=450, height=450)
col5.plotly_chart(fig5)

# 3. 지도 기반 대출 현황 (전체 너비 사용)
st.subheader("📍 지역별 대출 승인 및 부실율")
state_summary = df.groupby("addr_state").agg({"loan_amnt": "sum"}).reset_index()
fig6 = px.choropleth(state_summary, locations="addr_state", locationmode="USA-states",
                     color="loan_amnt", scope="usa",
                     title="지역별 대출 승인 및 부실율",
                     width=1200, height=600)
st.plotly_chart(fig6)

# 4. 연도별 대출 승인 추이 (전체 너비 사용)
st.subheader("📅 연도별 대출 승인 금액 추이")
df["issue_d"] = pd.to_datetime(df["issue_d"])  # 날짜 변환
df["year"] = df["issue_d"].dt.year
yearly_summary = df.groupby("year")["loan_amnt"].sum().reset_index()
fig7 = px.line(yearly_summary, x="year", y="loan_amnt",
               title="연도별 대출 승인 금액 추이",
               width=1200, height=500)
st.plotly_chart(fig7)

# 5. 대출 기간(Term)별 평균 이자율 (도넛 차트)
st.subheader("📊 대출 기간별 평균 이자율")

avg_interest_by_term = df.groupby("term")["int_rate"].mean().reset_index()
fig8 = px.pie(avg_interest_by_term, names="term", values="int_rate",
              title="대출 기간별 평균 이자율", hole=0.6,
              width=500, height=450)
st.plotly_chart(fig8)

#-------------------------------------------

# 대출받고 싶어요 버튼 (누르면 상품 소개 페이지로 이동)
if st.button("💳 대출 받고 싶어요!"):
    st.switch_page("pages/product.py")  # ✅ 상품 소개 페이지로 이동


# 🔙 홈으로 돌아가는 버튼
if st.button("🔙 홈으로 돌아가기"):
    st.switch_page("app.py")  # ✅ 홈으로 이동