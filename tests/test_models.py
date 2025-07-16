from app.models.recommendation import GiftRequest, GiftResponse

def test_gift_models():
    # GiftRequest 생성 테스트
    req = GiftRequest(keyword="친구 생일 선물")
    assert req.keyword == "친구 생일 선물"

    # GiftResponse 생성 테스트
    res = GiftResponse(recommended_gift="책", explanation="독서를 좋아해서")
    assert res.recommended_gift == "책"
    assert res.explanation == "독서를 좋아해서"

    print("Pydantic 모델 테스트 성공!")

if __name__ == "__main__":
    test_gift_models()
