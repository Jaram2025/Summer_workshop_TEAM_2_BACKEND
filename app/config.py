# app/config.py

import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수에서 Gemini API 키 가져오기
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
