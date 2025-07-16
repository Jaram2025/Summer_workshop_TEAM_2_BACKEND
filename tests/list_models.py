import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def list_available_models():
    try:
        models = genai.list_models()
        for model in models:
            print(f"{model.name} - 지원 기능: {model.supported_generation_methods}")
    except Exception as e:
        print("모델 목록 조회 중 오류 발생:", e)

if __name__ == "__main__":
    list_available_models()
