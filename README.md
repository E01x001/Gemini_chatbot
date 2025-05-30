# Gemini Chatbot

Streamlit과 Google의 Gemini-1.5-Flash 모델을 사용한 챗봇 애플리케이션입니다.

## 기능

- 사용자와 대화형 인터페이스
- Gemini AI를 통한 자연스러운 응답 생성
- 대화 컨텍스트 유지
- 실시간 응답 표시

## 설치 및 실행

1. 저장소 클론:
```bash
git clone <repository-url>
cd gamini_chatbot
```

2. 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

4. Gemini API 키 설정:
- `.streamlit/secrets.toml` 파일 생성
- 아래 내용 추가:
```toml
[secrets]
GEMINI_API_KEY = "your_api_key_here"
```

5. 앱 실행:
```bash
streamlit run app.py
```

## Streamlit Cloud 배포

1. GitHub에 코드 푸시
2. [Streamlit Cloud](https://streamlit.io/cloud)에서 새 앱 배포
3. 환경 변수 설정:
   - Streamlit Cloud 대시보드의 앱 설정에서 "Secrets" 섹션에 API 키 추가

## 주의사항

- API 키를 공개 저장소에 커밋하지 않도록 주의
- `.streamlit/secrets.toml` 파일은 `.gitignore`에 포함되어 있음 