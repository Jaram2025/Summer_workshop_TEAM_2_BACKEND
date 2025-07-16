from app.services.gemini_service import get_gift_recommendation

def test_gemini():
    user_info = {
        "birth_date": "1995-08-15",
        "gender": "여성",
        "age": 29,
        "job": "대학생",
        "relationship": "여자친구",
        "min_price": 20000,
        "max_price": 50000
    }

    result = get_gift_recommendation(user_info)
    print("응답 결과:")
    print(result)

if __name__ == "__main__":
    test_gemini()
