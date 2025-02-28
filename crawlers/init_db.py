import sqlite3
import os

# 📌 절대 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # VW 폴더 경로
DB_PATH = os.path.join(BASE_DIR, "data", "products.db")  # SQLite DB 경로

# 📌 데이터베이스 연결
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 📌 대출 상품 테이블 생성
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    상품명 TEXT PRIMARY KEY,
    플랫폼수수료 TEXT,
    최저금리 TEXT,
    최대금리 TEXT,
    최소한도 TEXT,
    최대한도 TEXT
)
""")

# 📌 샘플 데이터 삽입 (중복 방지)
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    sample_products = [
        ("개인 신용 대출", "연 4.5%", "신용 등급에 따라 차등 적용"),
        ("소상공인 대출", "연 3.8%", "사업 운영자를 위한 맞춤 대출"),
        ("주택 담보 대출", "연 2.9%", "부동산 담보 제공 시 가능"),
        ("자동차 대출", "연 5.2%", "신차 및 중고차 구입 시")
    ]
    cursor.executemany("INSERT INTO loan_products (name, rate, description) VALUES (?, ?, ?, ?)", sample_products)

# 📌 변경 사항 저장 후 종료
conn.commit()
conn.close()

print(f"✅ 데이터베이스 초기화 완료: {DB_PATH}")