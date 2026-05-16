from fastapi import APIRouter

router = APIRouter(prefix="/api/restock", tags=["restock"])

@router.get("/")
async def get_restock_alerts():
    return {"message": "Restock alerts endpoint"}
