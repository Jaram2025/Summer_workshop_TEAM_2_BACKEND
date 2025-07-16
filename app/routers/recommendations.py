from fastapi import APIRouter, HTTPException
from app.models.recommendation import GiftRequest, GiftResponse
from app.services.gemini_service import get_gift_recommendation

router = APIRouter()

@router.post("/recommend", response_model=GiftResponse)
async def recommend_gift(request: GiftRequest):
    user_info = request.model_dump()
    result = get_gift_recommendation(user_info)

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return GiftResponse(recommendations=result)
