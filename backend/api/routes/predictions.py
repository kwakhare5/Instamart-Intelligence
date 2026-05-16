from fastapi import APIRouter

router = APIRouter(prefix="/api/predictions", tags=["predictions"])

@router.get("/")
async def get_predictions():
    return {"message": "Predictions endpoint"}
