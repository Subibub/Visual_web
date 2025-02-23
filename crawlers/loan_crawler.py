import requests
from bs4 import BeautifulSoup
import sqlite3
import json


# JSON 파일에서 은행 URL 리스트 로드
with open("bank_list.json", "r", encoding="utf-8") as file:
    bank_list = json.load(file)

headers = {"User-Agent": "Mozilla/5.0"}

# 크롤링 함수 정의
def scrape_loan_products(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 요청 실패 시 예외 발생
        soup = BeautifulSoup(response.text, "html.parser")

        # 사이트 구조에 맞는 크롤링 로직 (수정 필요)
        loan_products = []
        for item in soup.select(".loan-item"):  # 📌 각 사이트에 맞게 CSS 선택자 변경 필요
            try:
                name = item.select_one(".loan-title").text.strip()
                rate = item.select_one(".loan-rate").text.strip()
                description = item.select_one(".loan-desc").text.strip()                
                loan_products.append((name, rate, description, image_url, url))
            except AttributeError:
                continue  # 정보가 없으면 스킵

        return loan_products

    except requests.exceptions.RequestException as e:
        print(f" {url} 크롤링 중 오류 발생: {e}")
        return []
    

# 대출 상품 정보 추출
loan_products = []
for bank in bank_list:
    bank_url = bank.get("url")
    print(f"🔍 {bank_url}에서 대출 상품 크롤링 중...")
    products = scrape_loan_products(bank_url)
    loan_products.extend(products)


# 데이터베이스 저장
def save_to_database(products):
    conn = sqlite3.connect("Users/isubin/VW/data/products.db")  # 📌 DB 파일은 `data/` 폴더에 저장
    cursor = conn.cursor()

    # 테이블 생성 (없을 경우)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rate TEXT,
        description TEXT,
        bank_url TEXT
    )
    """)

    # 기존 데이터 삭제 후 최신 데이터 삽입 (자동 갱신)
    cursor.execute("DELETE FROM loan_products")
    cursor.executemany("INSERT INTO loan_products (name, rate, description) VALUES (?, ?, ?)", products)

    conn.commit()
    conn.close()
    print(" 최신 대출 상품이 데이터베이스에 저장되었습니다.")

# 크롤링한 데이터 저장 실행
if loan_products:
    save_to_database(loan_products)
else:
    print(" 크롤링된 데이터가 없습니다.")
