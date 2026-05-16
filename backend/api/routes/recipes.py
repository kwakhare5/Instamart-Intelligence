from fastapi import APIRouter

router = APIRouter(prefix="/api/recipes", tags=["recipes"])

@router.get("/")
async def get_recipes():
    return {"message": "Recipes endpoint"}
