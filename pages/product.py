import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="P2P 대출 상품 소개", page_icon="💳")

# 🎯 상품 소개 페이지
st.title("💳 P2P 대출 상품 안내")
st.write("""
P2P 대출(Peer-to-Peer Lending)은 금융기관을 거치지 않고 투자자와 차입자가 직접 연결되는 대출 방식입니다.
국내 대표 P2P 대출 플랫폼(테라펀딩, 렌딧, 8퍼센트 등)의 상품을 참고하여 다양한 대출 옵션을 제공합니다.
""")

# 📌 P2P 대출 상품 정보 (예제 데이터)
p2p_products = pd.DataFrame({
    "상품명": ["일반 신용 대출", "부동산 담보 대출", "소상공인 대출", "자동차 담보 대출"],
    "대출 한도": ["최대 5,000만 원", "최대 10억 원", "최대 2억 원", "최대 1억 원"],
    "이자율": ["연 6~12%", "연 5~9%", "연 7~15%", "연 4~8%"],
    "신용 점수 기준": ["600점 이상", "담보 평가 기준", "550점 이상", "차량 감정가 기준"],
    "상환 기간": ["12~60개월", "24~120개월", "6~36개월", "12~60개월"],
    "플랫폼": ["렌딧, 8퍼센트", "테라펀딩, 루트에너지", "팝펀딩, 와디즈", "피플펀드, 테라펀딩"]
})

# 📌 상품 정보 테이블 표시
st.subheader("📌 P2P 대출 상품 목록")
st.dataframe(p2p_products)

#----------------------------
# 이자율 데이터 정리 함수
def clean_interest_rate(rate):
    rate = rate.replace("연 ", "").replace("%", "")  # "연 " 및 "%" 제거
    if "~" in rate:
        low, high = map(float, rate.split("~"))  # 범위가 있을 경우 평균값 계산
        return (low + high) / 2
    return float(rate)  # 단일 값이면 float 변환

# 이자율 변환 적용
p2p_products["평균 이자율"] = p2p_products["이자율"].apply(clean_interest_rate)

# Streamlit 대시보드 설정
st.title("📊 P2P 대출 상품 비교 대시보드")

# 평균 이자율 바 차트
st.subheader("📊 P2P 대출 상품별 평균 이자율 비교")
st.bar_chart(p2p_products.set_index("상품명")["평균 이자율"])

# 📌 P2P 투자자의 역할 설명
st.subheader("📌 P2P 투자자의 역할")
st.write("""
P2P 금융에서 투자자는 차입자의 대출에 자금을 공급하며, 일정한 이자 수익을 기대할 수 있습니다.
각 상품별 투자자 모집 방식이 다르며, 신용 평가 및 담보 평가가 이루어진 후 투자자가 모집됩니다.
""")

st.subheader("📌 주요 P2P 금융사")
st.write("""
- **렌딧**: 개인 신용 대출 중심의 P2P 금융 플랫폼
- **8퍼센트**: 개인 및 소상공인을 위한 중금리 대출
- **테라펀딩**: 부동산 담보 대출 전문 P2P 금융사
- **팝펀딩**: 중소기업 및 개인 사업자 대출 플랫폼
- **와디즈**: 크라우드펀딩과 P2P 금융이 결합된 모델
- **피플펀드**: 자동차 및 다양한 자산 기반 대출 상품 제공
""")

# 🔙 홈으로 돌아가는 버튼
if st.button("🔙 홈으로 돌아가기"):
    st.switch_page("app.py")  # ✅ 홈으로 이동