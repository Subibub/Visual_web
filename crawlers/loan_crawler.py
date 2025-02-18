import requests
from bs4 import BeautifulSoup
import sqlite3

# 📌 크롤링할 은행 대출 상품 페이지 URL (실제 은행 웹사이트로 변경 필요)
URL = "https://8percent.kr/"

# 📌 웹 페이지 요청
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 📌 대출 상품 정보 추출
loan_products = []
for item in soup.select(".loan-item"):  # CSS 선택자 변경 (사이트 구조에 맞게)
    name = item.select_one(".loan-title").text.strip()
    rate = item.select_one(".loan-rate").text.strip()
    description = item.select_one(".loan-desc").text.strip()
    image_url = item.select_one("img")["src"]  # 상품 이미지 URL

    loan_products.append((name, rate, description, image_url))

# ✅ 데이터베이스 저장
def save_to_database(products):
    conn = sqlite3.connect("Users/isubin/VW/data/products.db")  # 📌 DB 파일은 `data/` 폴더에 저장
    cursor = conn.cursor()

    # 기존 데이터 삭제 후 최신 데이터 삽입 (자동 갱신)
    cursor.execute("DELETE FROM loan_products")
    cursor.executemany("INSERT INTO loan_products (name, rate, description, image_url) VALUES (?, ?, ?, ?)", products)

    conn.commit()
    conn.close()
    print("✅ 최신 대출 상품이 데이터베이스에 저장되었습니다.")

# ✅ 크롤링한 데이터 저장 실행
save_to_database(loan_products)