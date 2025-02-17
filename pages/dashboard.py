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

#대출 승인 및 조건분석 
#대출 금액vs 이자율 
st.subheader("대출 금액 대비 이자율")
fig0 = px.scatter(df, x="loan_amnt", y="int_rate", color="grade", title="대출 금액 대비 이자율")
st.plotly_chart(fig0)

# 📊 신용등급 vs 이자율 (산점도)
st.subheader("📊 신용 등급 vs. 이자율")
fig1 = px.scatter(df, x="grade", y="int_rate",
                  size="loan_amnt", color="int_rate",
                  title="신용 등급 vs 이자율급",
                  labels={"grade": "신용 등급", "int_rate": "이자율 (%)"})
st.plotly_chart(fig1)
# 신용세부등급 vs 이자율
st.subheader("신용세부 등급 vs 이자율")
fig2 = px.scatter(df, x="sub_grade", y="int_rate", color="loan_amnt", title="신용세부 등급 vs 이자율")
st.plotly_chart(fig2)

#신용점수 분포 
fig3 = px.histogram(df, x="fico_avg", nbins=30, title="신용 점수 분포", color_discrete_sequence=["#FF6F61"])
st.plotly_chart(fig3, use_container_width=True)

#신용점수 vs 대출금액
fig4 = px.scatter(df, x="fico_avg", y="loan_amnt", color="int_rate", title="신용 점수 vs 대출 금액")
st.plotly_chart(fig4)

#신용점수 vs 이자율 
st.subheader("신용 점수 vs 이자율")
fig5 = px.scatter(df, x="fico_avg", y="int_rate", color="loan_amnt", title="신용 점수 vs 이자율")
st.plotly_chart(fig5)


#대출상환기간 vs 이자율, 대출금액 
fig6 = px.scatter(df, x="term", y="int_rate", title="대출 상환 기간 vs 이자율")
st.plotly_chart(fig6)

#-------------------------------------------
#대출자 특성과 대출 조건 

#고용기간 vs 대출승인 조건 
st.subheader("고용기간 대비 대출 승인 조건")
fig7 = px.scatter(df, x="emp_length", y="loan_amnt", color="int_rate", title="고용기간 대비 대출 승인 조건")
st.plotly_chart(fig7)

# 📊 연소득 vs 대출 금액 (Altair 산점도)
st.subheader("📊 연소득 vs. 대출 금액")
chart = alt.Chart(df).mark_circle().encode(
    x="annual_inc",
    y="loan_amnt",
    size="loan_amnt",
    color="int_rate",
    tooltip=["annual_inc", "loan_amnt", "grade", "int_rate"]
).properties(title="연소득 vs. 대출 금액", width=700, height=400)
st.altair_chart(chart)

# 📊 대출 금액 분포 (Matplotlib 히스토그램)
st.subheader("📊 대출 금액 분포")
plt.figure(figsize=(8, 4))
plt.hist(df["loan_amnt"], bins=20, color="skyblue", edgecolor="black")
plt.xlabel("대출 금액 ($)")
plt.ylabel("빈도")
plt.title("대출 금액 분포")
st.pyplot(plt)

#집소유 여부에 따른 대출조건 차이 
st.subheader("집 소유 여부에 따른 대출 조건 차이")
fig8 = px.bar(df, x="home_ownership", y="loan_amnt", color="grade", title="집 소유 여부에 따른 대출 조건 차이")
st.plotly_chart(fig8)
#-------------------------------------------
#상환성공률 및 연체 분석 
#대출목적에 따른 연체여부
st.subheader("대출 목적에 따른 연체 여부")
fig9 = px.histogram(df, x="purpose", color="loan_status", title="대출 목적에 따른 연체 여부")
st.plotly_chart(fig9)

#연체여부에 따른 이자율의 평균을 파이차트로 나타내기
st.subheader("연체 여부에 따른 이자율 평균")
st.write(df.groupby("loan_status")["int_rate"].mean())
fig9_1 = px.pie(df, names="loan_status", values="int_rate", title="연체 여부에 따른 이자율 평균")
st.plotly_chart(fig9_1)


#대출자들의 총 부채와 상환가능성 
st.subheader("대출자들의 총 부채와 상환 가능성")
fig10 = px.scatter(df, x="total_acc", y="loan_amnt", color="int_rate", title="대출자들의 총 부채와 상환 가능성")
st.plotly_chart(fig10)
#-------------------------------------------
#지역별 분석 
#대출지역 선택해서 보기 
selected_states = st.multiselect("📍 대출 지역 선택", df["addr_state"].unique())
filtered_df = df[df["addr_state"].isin(selected_states)]
fig11 = px.histogram(filtered_df, x="loan_amnt", nbins=20, title="선택된 지역의 대출 금액 분포")
st.plotly_chart(fig11)

#지도에서 지역별 평균임금,주택보유비율, 연체비율, 대출금액 확인하기 
st.subheader("지도에서 지역별 평균임금, 주택보유비율, 연체비율, 대출금액 확인하기")
st.write("""
지도에서 지역별 평균임금, 주택보유비율, 연체비율, 대출금액을 확인할 수 있습니다.
""")
#지도에 나타낼 데이터 선택
data_type = st.selectbox("지도에 나타낼 데이터 선택", ["평균임금", "주택보유비율", "연체비율", "대출금액"])
if data_type == "평균임금":
    fig12 = px.choropleth(df, locations="addr_state", locationmode="USA-states", color="annual_inc", scope="usa", title="지역별 평균임금")
elif data_type == "주택보유비율":
    fig12 = px.choropleth(df, locations="addr_state", locationmode="USA-states", color="home_ownership", scope="usa", title="지역별 주택보유비율")
elif data_type == "연체비율":
    fig12 = px.choropleth(df, locations="addr_state", locationmode="USA-states", color="delinq_2yrs", scope="usa", title="지역별 연체비율")
else:
    fig12 = px.choropleth(df, locations="addr_state", locationmode="USA-states", color="loan_amnt", scope="usa", title="지역별 대출금액")
st.plotly_chart(fig12)



#-------------------------------------------
#금융습관 유형 
#리볼빙 많은 사람들의 연체비율 
st.subheader("리볼빙 많은 사람들의 연체 비율")
fig13 = px.scatter(df, x="revol_bal", y="delinq_2yrs", color="grade", title="리볼빙 많은 사람들의 연체 비율")
st.plotly_chart(fig13)

#현재 계좌 개수와 연체율 
st.subheader("현재 계좌 개수와 연체율")
fig14 = px.scatter(df, x="open_acc", y="delinq_2yrs", color="int_rate", title="현재 계좌 개수와 연체율")
st.plotly_chart(fig14)

#이자율과 대출자의 행동패턴 분석(이자율 높을 수록 연체하는지 파악하기) 
st.subheader("이자율과 대출자의 행동 패턴 분석")
fig15 = px.scatter(df, x="int_rate", y="delinq_2yrs", color="grade", title="이자율과 대출자의 행동 패턴 분석")
st.plotly_chart(fig15)



#-------------------------------------------

# 대출받고 싶어요 버튼 (누르면 상품 소개 페이지로 이동)
if st.button("💳 대출 받고 싶어요!"):
    st.switch_page("pages/product.py")  # ✅ 상품 소개 페이지로 이동


# 🔙 홈으로 돌아가는 버튼
if st.button("🔙 홈으로 돌아가기"):
    st.switch_page("app.py")  # ✅ 홈으로 이동