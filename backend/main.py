from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import household, predictions, restock, recipes
from backend.database.connection import init_db
import uvicorn

app = FastAPI(title="Instamart Intelligence API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(household.router)
app.include_router(predictions.router)
app.include_router(restock.router)
app.include_router(recipes.router)

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/")
async def root():
    return {"message": "Welcome to Instamart Intelligence API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
