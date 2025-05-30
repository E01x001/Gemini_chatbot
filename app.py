# ✅ Streamlit Cloud에서 API 키를 사용하려면 .streamlit/secrets.toml 또는 웹 대시보드의 Secrets 설정에 아래와 같은 형식으로 키를 입력해야 합니다.
#
# [secrets]
# GEMINI_API_KEY = "your_api_key_here"

import streamlit as st
import google.generativeai as genai

# API 키 설정
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception as e:
    st.error("⚠️ Gemini API 키가 설정되지 않았습니다. .streamlit/secrets.toml 파일에 API 키를 설정해주세요.")
    st.error(f"에러 상세: {str(e)}")
    st.stop()

# Gemini API 설정
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# 페이지 설정
st.set_page_config(page_title="Gemini Chatbot", layout="wide")
st.title("Gemini Chatbot")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 채팅 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
user_input = st.chat_input("메시지를 입력하세요")

# 메시지 처리
if user_input:
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    try:
        # 응답 생성 중임을 표시
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("🤔 생각하는 중...")
            
            # Gemini API로 응답 생성
            response = st.session_state.chat.send_message(user_input)
            assistant_response = response.text
            
            # 응답 표시
            message_placeholder.markdown(assistant_response)
        
        # 메시지 저장
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
    except Exception as e:
        error_message = f"⚠️ 오류가 발생했습니다: {str(e)}"
        with st.chat_message("assistant"):
            st.error(error_message)
        st.session_state.messages.append({"role": "assistant", "content": error_message})
