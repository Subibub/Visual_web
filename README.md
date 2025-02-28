## 웹페이지 목적 
  랜딩클럽의 고객들이 정보 파악 용이 + 대출 및 투자 진행할 수 있도촉  1) 대출자 2)투자자 
  로그인 하게되면 랜딩클럽의 유저(=회사 직원)들이 고객들 데이터 쉽게 볼 수 있도록 
## 프로젝트 구조

├── crawlers            # 데이터 크롤러 및 자동 업데이트 스크립트
│   ├── auto_update.py  # 일정 시간마다 크롤러 실행 (스케줄링)
│   ├── bank_list.json  # 대출 상품 제공 기관 목록
│   ├── init_db.py      # 데이터베이스 스크립트
│   ├── loan_crawler.py # 대출 상품 정보를 크롤링하는 스크립트
│
├── data                # 웹페이지 필요한 data 폴더 
│   ├── products.db     # SQLite 데이터베이스 (대출 상품 정보 저장)
│   ├── assets.png      # 이미지 및 리소스
│   ├── fund.png        # 이미지 및 리소스
│   ├── invest.png      # 이미지 및 리소스
│   ├── logo.png        # 이미지 및 리소스
│   ├── Customer_data.csv     # 고객관련 데이터
│   ├── User_data.csv     # 회사관련 데이터 (데이터가 더 많이 가공됨)
│
├── pages               # Streamlit 웹 애플리케이션 페이지
│   ├── company.py      # 회사가 필요한 정보 시각화 페이지 
│   ├── cs.py           # 고객센터 페이지
│   ├── dashboard.py    # 고객 유저에게 필요한 정보 시각화 페이지
│   ├── invest.py       # 투자 상품 정보 페이지
│   ├── loan_product.py # 대출 상품 정보 페이지
│   ├── search_credit.py # 금리 및 한도 조회 페이지 
│
├── venv                # 가상 환경 (Python Virtual Environment)
├── app.py              # 홈페이지 
├── login_handler.py    # 사용자 로그인 및 인증 기능
├── navigation.py       # 네비게이션 메뉴 및 페이지 이동
├── requirements.txt    # 프로젝트 의존성 목록 (Python 패키지)
└── README.md           # 프로젝트 설명 파일
