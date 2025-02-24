import streamlit as st
import time

def init_login_state():
    """세션 상태 초기화"""
    if "show_login" not in st.session_state:
        st.session_state.show_login = False
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

def handle_login():
    """로그인 UI 및 처리"""
    if st.query_params.get("login") == "true":
        st.session_state.show_login = True

    if st.session_state.show_login and not st.session_state.logged_in:
        st.markdown("### 로그인")

        username = st.text_input("아이디:")
        password = st.text_input("비밀번호:", type="password")

        if st.button("로그인"):
            if username == "admin" and password == "1234":  # 예제 로그인 검증
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.show_login = False
                st.success("✅ 로그인 성공! 회사 페이지로 이동합니다.")
                time.sleep(1)  # 성공 메시지를 보여줄 시간 확보
                st.query_params.clear()  # Query 파라미터 초기화
                st.switch_page("pages/company.py")  # 회사 페이지로 이동

def handle_logout():
    """로그아웃 버튼 UI 및 처리"""
    if st.session_state.logged_in:
        st.sidebar.write(f"👤 {st.session_state.username} 님")
        if st.sidebar.button("🚪 로그아웃"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.success("로그아웃 되었습니다.")
            time.sleep(1)
            st.rerun()  # 페이지 새로고침