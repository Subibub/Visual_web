import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="대출 데이터 대시보드",layout="wide")

# 스타일 적용 
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .top-nav {
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
        .sub-navbar {
            text-align: center;
            font-size: 18px;
            padding: 10px;
            border-bottom: 2px solid #ddd;
        }
        .popup {
            background-color: #2c2c2c;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 네비게이션 바
st.markdown(
    """
    <div class="top-nav">
        <a href="/" style="text-decoration: none; color: black;">LENDIT</a>
    </div>
    <div class="sub-navbar">
        LendingClub 시각화
    </div>
    <br><br><br><br>
    """,
    unsafe_allow_html=True
)

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
        type.error("데이터 파일을 찾을 수 없습니다. 샘플 데이터를 사용합니다.")
    return df

df = load_data()


#================================================================================================
#대시보드 생성
#주요 금융 지표 요약
st.subheader(" 주요 금융 지표")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("평균 이자율", f"{df['int_rate'].mean():.2f}%")
with col2:
    st.metric("평균 대출 금액", f"${df['loan_amnt'].mean():,.0f}")
with col3:
    st.metric("평균 신용 점수", f"{df['fico_avg'].mean():.0f}")

#공간 여유 확보 
st.write("")
st.write("")

#-------------------------------------------
#주제별 시각화 
# 1. 대출 상태별 
st.subheader(" 대출 상태별 분석")
col1, col2, col3 = st.columns([1, 1, 1])  # 3개 컬럼 배치

fig1 = px.pie(df, names="loan_status", title="대출 연체 비율", width=400, height=400)
col1.plotly_chart(fig1)

# 대출 상태별 평균 신용 점수 및 평균 이자율 계산
loan_status_avg = df.groupby("loan_status").agg({"fico_avg": "mean", "int_rate": "mean"}).reset_index()

# 대출 상태별 평균 신용 점수 시각화
fig1_1 = px.bar(loan_status_avg, x="loan_status", y="fico_avg", color="loan_status",
                title="대출 상태별 평균 신용 점수", 
                labels={"fico_avg": "평균 신용 점수", "loan_status": "대출 상태"},
                width=400, height=400)
col2.plotly_chart(fig1_1)

# 대출 상태별 평균 이자율 시각화
fig1_2 = px.bar(loan_status_avg, x="loan_status", y="int_rate", color="loan_status",
                title="대출 상태별 평균 이자율", 
                labels={"int_rate": "평균 이자율 (%)", "loan_status": "대출 상태"},
                width=400, height=400)
col3.plotly_chart(fig1_2)

#-------------------------------------------
# 2. 이자율 
st.subheader(" 이자율 분석")
col1, col2 = st.columns([1, 1])  # 3개 컬럼 배치
fig2_1 = px.scatter(df, x="fico_avg", y="int_rate", color="loan_amnt",
                  title=" 신용 점수 vs 이자율",
                  labels={"fico_avg": "신용 점수", "int_rate": "이자율 (%)"},
                  width=400, height=400)
col1.plotly_chart(fig2_1)

avg_values = df.groupby("grade").agg({"loan_amnt": "mean", "int_rate": "mean"}).reset_index()
fig2_2 = px.bar(avg_values, x="grade", y=["loan_amnt", "int_rate"], barmode="group",
              title="등급별 평균 대출 금액 & 평균 이자율",
              width=400, height=400)
col2.plotly_chart(fig2_2)

# 팝업 창 - 신용 점수 입력
if "popup" not in st.session_state:
    st.session_state.popup = False

if st.button("나의 신용 점수 입력"):
    st.session_state.popup = True

if st.session_state.popup:
    with st.form("user_info_form"):
        fico_score = st.slider("내 신용 점수 입력", 300, 850, 700)
        submitted = st.form_submit_button("확인")
        if submitted:
            st.session_state.popup = False
            
            # ±10 범위 내 신용 점수 데이터 찾기
            filtered_df = df[(df["fico_avg"] >= fico_score - 10) & (df["fico_avg"] <= fico_score + 10)]
            
            if filtered_df.empty:
                st.write("해당 신용 점수를 가진 데이터가 없습니다.")
            else:
                avg_loan = filtered_df["loan_amnt"].mean()
                avg_rate = filtered_df["int_rate"].mean()
                st.subheader("나와 비슷한 신용 점수의 평균 대출 금액 & 이자율")
                st.metric("평균 대출 금액", f"${avg_loan:,.0f}")
                st.metric("평균 이자율", f"{avg_rate:.2f}%")

# 평행 좌표 그래프 생성
# 사용자가 보고 싶은 신용 점수 범위 선택
fico_min, fico_max = st.slider("신용 점수 범위 선택", min_value=int(df["fico_avg"].min()), 
                               max_value=int(df["fico_avg"].max()), value=(650, 800))

# 선택한 신용 점수 범위로 데이터 필터링
filtered_df = df[(df["fico_avg"] >= fico_min) & (df["fico_avg"] <= fico_max)]

# 평행 좌표 그래프 생성 (신용 점수를 색상 기준으로 설정)
fig3_1 = px.parallel_coordinates(filtered_df,
                                 dimensions=["loan_amnt", "int_rate", "dti", "fico_avg"],
                                 color="fico_avg",  # 신용 점수를 색상 기준으로 변경
                                 labels={"loan_amnt": "대출 금액 ($)",
                                         "int_rate": "이자율 (%)",
                                         "dti": "부채 비율 (DTI)",
                                         "fico_avg": "신용 점수 (FICO)"},
                                 color_continuous_scale="Blues")  # 파란 계열 색상 적용

# 그래프 크기 및 제목 조정
fig3_1.update_layout(title_text="LendingClub 대출 특성 평행 좌표 그래프",
                     font_size=14, title_font_size=16, height=500)
st.plotly_chart(fig3_1)

#-------------------------------------------
# 2.대출 목적(Treemap) & 주택 소유별 대출 금액
st.subheader("대출 목적 및 주택 소유별 대출 금액")
col4, col5 = st.columns([1.5, 1])  # 첫 번째 컬럼을 더 넓게 설정
# 대출 목적별 평균 대출 금액 계산
purpose_avg = df.groupby("purpose")["loan_amnt"].mean().reset_index()

fig4 = px.treemap( purpose_avg, path=["purpose"], values="loan_amnt",
                  title="대출 목적별 평균 대출 금액",
                  width=600, height=450)
#트리맵 설정 
fig4.update_traces(
    textinfo="label+value+percent entry",  # 대출 목적 + 평균 대출 금액 + 비율(%)
    insidetextfont=dict(size=14)  # 글자 크기 변경
)
col4.plotly_chart(fig4)

avg_home_loan = df.groupby("home_ownership")["loan_amnt"].mean().reset_index()
fig5 = px.bar(avg_home_loan, x="home_ownership", y="loan_amnt",
              title="주택 소유별 평균 대출 금액",
              color="home_ownership",
              width=450, height=450)
col5.plotly_chart(fig5)

#-------------------------------------------
# 3. 지도 기반 대출 현황 (전체 너비 사용)
st.subheader("지역별 분석")
state_summary = df.groupby(["addr_state"]).agg({
    "loan_amnt": "mean",
    "int_rate": "mean",
    "loan_status": lambda x: (x == 1).mean() * 100  # 승인율 계산
}).reset_index()
state_summary.rename(columns={"loan_status": "Delinquency_rate"}, inplace=True)

# 지도 기반 대출 현황 시각화
fig6 = px.choropleth(state_summary, locations="addr_state", locationmode="USA-states",
                     color="Delinquency_rate",
                     hover_name="addr_state",
                     hover_data={"loan_amnt": True, "int_rate": True, "Delinquency_rate": True},
                     scope="usa", title="지역별 부실율 및 대출현황 ",
                     width=1200, height=600, color_continuous_scale="Blues")

st.plotly_chart(fig6)

#-------------------------------------------
# 4. 연도별 대출 승인 추이 (전체 너비 사용)
st.subheader("연도별 대출 승인 금액 추이")
df["issue_d"] = pd.to_datetime(df["issue_d"])  # 날짜 변환
df["year"] = df["issue_d"].dt.year
yearly_summary = df.groupby("year")["loan_amnt"].sum().reset_index()
fig7 = px.line(yearly_summary, x="year", y="loan_amnt",
               title="연도별 대출 승인 금액 추이",
               width=1200, height=500)
st.plotly_chart(fig7)

#-------------------------------------------
# 5. 대출 기간(Term)별 분석 
col6, col7 = st.columns([1, 1])  # 첫 번째 컬럼을 더 넓게 설정

st.subheader("대출 기간별 분석")

avg_interest_by_term = df.groupby("term")["int_rate"].mean().reset_index()
fig8 = px.pie(avg_interest_by_term, names="term", values="int_rate",
              title="대출 기간별 평균 이자율", hole=0.6,
              width=500, height=450)
col6.plotly_chart(fig8)

# 반원게이트 차트 만들기 -대출기간별 평균 대출 금액 
avg_amt_by_term = df.groupby("term")["loan_amnt"].mean().reset_index()
fig8_1 = px.pie(avg_amt_by_term, names="term", values="loan_amnt",
               title="대출 기간별 평균 대출 금액", hole=0.6,
               width=500, height=450)
col7.plotly_chart(fig8_1)


#-------------------------------------------
# loan_status가 0(완납) / 1(연체)로 표시됨 → 연체율 계산
df_term_summary = df.groupby("term")["loan_status"].mean().reset_index()
df_term_summary.columns = ["term", "default_rate"]
df_term_summary["default_rate"] *= 100  # 백분율 변환

#  사용자가 대출 기간 선택 (36개월 or 60개월)
selected_term = st.radio("대출 기간 선택", df_term_summary["term"].tolist())

# 선택한 기간에 해당하는 부실율 값 가져오기
selected_rate = df_term_summary[df_term_summary["term"] == selected_term]["default_rate"].values[0]

# 반원 게이지 차트 만들기
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=selected_rate,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': f"{selected_term}기간 연체율 (%)"},
    gauge={
        "axis": {"range": [0, 50]},  # 0~50% 부실율 범위
        "bar": {"color": "darkblue"},  # 바 색상
        "steps": [
            {"range": [0, 15], "color": "green"},
            {"range": [15, 30], "color": "orange"},
            {"range": [30, 50], "color": "red"}
        ],
        "shape": "angular"
    }
))

# 레이아웃 변경 (반원 형태로 만들기)
fig.update_layout(
    height=400,  # 차트 높이 조정
    margin=dict(l=20, r=20, t=50, b=0)  # 여백 조정
)

# 반원 게이지 차트 출력
st.plotly_chart(fig)

# 추가 정보 출력
st.markdown(f"### 🔍 {selected_term} 대출의 평균 부실율: **{selected_rate:.2f}%**")
#-------------------------------------------
# 6. 대출 금액별 연간 소득 분포 (박스플롯)
st.subheader("대출 금액별 연간 소득 분포")
# 연소득을 일정 구간으로 나누기
bins = [0, 50000, 100000, 150000, 200000, 300000, df["annual_inc"].max()]
labels = ["0-50K", "50K-100K", "100K-150K", "150K-200K", "200K-300K", "300K+"]

df["income_group"] = pd.cut(df["annual_inc"], bins=bins, labels=labels)

# 각 그룹별 평균 대출 금액 계산
grouped_df = df.groupby("income_group")["loan_amnt"].mean().reset_index()
grouped_df = grouped_df.sort_values("loan_amnt", ascending=False)
fig9 = px.box(df, x="income_group", y="loan_amnt",
             title="소득 수준별 대출 금액 분포",
             points="all")  # 개별 데이터 점 표시
st.plotly_chart(fig9)


#-------------------------------------------

# 대출받고 싶어요 버튼 (누르면 상품 소개 페이지로 이동)
if st.button("💳 대출 받고 싶어요!"):
    st.switch_page("pages/product.py")  # ✅ 상품 소개 페이지로 이동


# 🔙 홈으로 돌아가는 버튼
if st.button("🔙 홈으로 돌아가기"):
    st.switch_page("app.py")  # ✅ 홈으로 이동