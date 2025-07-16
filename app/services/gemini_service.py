import json
import re
import google.generativeai as genai
from app.config import GEMINI_API_KEY

# Gemini API 키 설정
genai.configure(api_key=GEMINI_API_KEY)

# 사용할 모델 (지원되는 최신 모델 중 하나)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_prompt(user_info: dict) -> str:
    return f"""
당신은 선물 추천 도우미입니다.

사용자 정보:
- 생일: {user_info['birth_date']}
- 성별: {user_info['gender']}
- 나이: {user_info['age']}세
- 직업: {user_info['job']}
- 선물 대상자와의 관계: {user_info['relationship']}
- 희망 가격대: {user_info['price_min']}원 ~ {user_info['price_max']}원

이 정보를 바탕으로 해당 대상자에게 적절한 선물을 3가지 추천해 주세요.
일반적인 물건 대신 쿠팡이나 아마존 등 실제 플랫폼에서 구매할 수 있는 상품명을 사용해주세요.

각 선물은 다음 JSON 형식으로 구성해주세요:

{{
"product_name": "string (실제 제품명/브랜드 포함)",
"approx_price_krw": "integer (예산 내에서 구체적인 가격)",
"reason": "string (추천 이유)"
}}

모든 설명은 한국어로 작성하고, JSON 배열로 3개의 선물을 반환해주세요.
"""

def clean_response_text(text: str) -> str:
    """
    Gemini가 보내는 응답에 포함된 마크다운 코드블록 제거
    ex) ```json ... ```
    """
    # 정규식으로 앞뒤 ```json 및 ``` 제거
    cleaned = re.sub(r"^```json\s*|```$", "", text.strip(), flags=re.MULTILINE)
    return cleaned.strip()

def get_gift_recommendation(user_info: dict) -> list:
    try:
        prompt = generate_prompt(user_info)
        response = model.generate_content(prompt)

        raw_text = response.text
        print("Gemini raw response:", raw_text)

        cleaned_text = clean_response_text(raw_text)
        print("Cleaned response:", cleaned_text)

        data = json.loads(cleaned_text)
        return data

    except json.JSONDecodeError as je:
        print("JSONDecodeError:", je)
        return {"error": "Gemini 응답이 JSON 형식이 아닙니다", "detail": str(je)}
    except Exception as e:
        print("Exception:", e)
        return {"error": str(e)}
