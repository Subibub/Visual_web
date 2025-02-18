import schedule
import time
import os

# 📌 24시간마다 웹 크롤러 실행
def update_loan_products():
    os.system("python VW/crawlers/loan_crawler.py")  # 크롤러 실행

# 매일 실행
schedule.every().day.at("03:00").do(update_loan_products)  # 매일 새벽 3시에 실행

while True:
    schedule.run_pending()
    time.sleep(60)  # 1분마다 체크