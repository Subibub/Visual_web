import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# 페이지 설정
st.set_page_config(page_title="P2P 대출 상품", layout="wide")

# Lottie 애니메이션 불러오기
lottie_url = "https://assets3.lottiefiles.com/packages/lf20_kxsd2ytq.json"

def load_lottie(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

lottie_animation = load_lottie(lottie_url)

# 네비게이션 바
st.markdown(
    """
    <style>
        .top-nav {
            background-color: #E3F2FD;
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
        <a href="/" style="text-decoration: none; color: white;">LENDIT</a>
    </div>
    """,
    unsafe_allow_html=True
)


# 배경 스타일 적용 (높이를 더 크게 조정)
st.markdown(
    """
    <div style="background-color:#E3F2FD; padding: 100px; display: flex; align-items: center;">
        <div style="flex: 1;">
            <h2>합리적인 금리로 빠르고 안전한 대출!</h2>
            <p>신뢰할 수 있는 금융 상품을 통해 최적의 대출을 찾아보세요.</p>
        </div>
        <div style="flex: 1; text-align: right;">
            <img src="https://cdn-icons-png.flaticon.com/512/2331/2331941.png" alt="People Icon"/>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)



# 상품 데이터 업데이트
data = {
    "상품명": ["개인신용대출", "직장인신용대출", "부동산 담보 대출", "소상공인 대출", "자동차 담보 대출"],
    "플랫폼 수수료": ["연 2% 이내", "최대 연 5%", "연 1.7%", "연 2.4%", "연 2~6% 이내"],
    "최저금리": ["연 5.0%", "연 4.21%", "연 5.0%", "연 7.0%", "연 4.0%"],
    "최대금리": ["연 18.0%", "연 17.9%", "연 9%", "연 15%", "연 8%"],
    "최소한도": ["100만 원", "200만 원", "-", "-", "-"],
    "최대한도": ["1억 원", "5,000만 원", "최대 10억 원", "최대 2억 원", "최대 1억 원"]
}

# 상품별 맞춤 아이콘 매칭
icon_urls = {
    "개인신용대출": "https://img.icons8.com/ios-filled/50/4A90E2/user.png",
    "직장인신용대출": "https://img.icons8.com/ios-filled/50/4A90E2/briefcase.png",
    "부동산 담보 대출": "https://img.icons8.com/ios-filled/50/4A90E2/home.png",
    "소상공인 대출": "https://img.icons8.com/ios-filled/50/4A90E2/shop.png",
    "자동차 담보 대출": "https://img.icons8.com/ios-filled/50/4A90E2/car.png",
}

df = pd.DataFrame(data)

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
                    <img src="{icon_urls[item["상품명"]]}" alt="Loan Icon"/>
                    <h3 style="color: #4A90E2;">{item["상품명"]}</h3>
                    <p><strong>최저금리:</strong> {item["최저금리"]}</p>
                    <p><strong>최대한도:</strong> {item["최대한도"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )




