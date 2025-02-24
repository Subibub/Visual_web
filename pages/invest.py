import streamlit as st
import pandas as pd
import requests


# 페이지 설정
st.set_page_config(page_title="LendSure 투자상품", layout="wide")


# 네비게이션 바
st.markdown(
    """
    <style>
        .top-nav {
            background-color: #9bb2e8;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
    </style>    
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="top-nav">
        <a href="/" style="text-decoration: none; color: white;">LENDSURE</a>
    </div>
    """,
    unsafe_allow_html=True
)


# 배경 스타일 적용 (높이를 더 크게 조정)
st.markdown(
    """
    <div style="background-color:#9bb2e8; padding: 100px; display: flex; align-items: center;">
        <div style="flex: 1;">
            <h2>수익성과 안정성을 모두 고려한 렌드슈어의 투자</h2>
            <p>데이터로 입증된 투자,렌드슈어와 함께 수익성과 안정성을 극대화하세요!</p>
        </div>
        <div style="flex: 1; text-align: right;">
        <img src="https://cdn-icons-png.flaticon.com/512/1041/1041916.png" class="header-icon">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)



# 상품 데이터 업데이트

# 투자 상품 데이터 예시 (CSV, JSON 활용 가능)
invest_data = {
    "상품명": ["아파트", "아파트","아파트", "증권", "신용"],
    "연 수익률": ["11.4", "14.5%", "8.5%", "8.5%", "14.9"],
    "유효담보비율": ["52.33%", "60.83%","24.30%", "-", "-"],
    "투자기간": ["12개월", "12개월", "12개월", "3개월", "48개월"],
    "모집금액": ["6000만 원", "2000만 원", "5000만 원","3000만원", "3000만 원"]
}

df = pd.DataFrame(invest_data)

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
            color: #4A90E2;
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
                    <h3 style="color: #4A90E2;">{item["상품명"]}</h3>
                    <p><strong>연 수익률:</strong> {item["연 수익률"]}</p>
                    <p><strong>유효담보비율:</strong> {item["유효담보비율"]}</p>
                    <p><strong>투자기간:</strong> {item["투자기간"]}</p>
                    <p><strong>모집금액:</strong> {item["모집금액"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )



