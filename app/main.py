from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from database import engine, Base
import logging
import uvicorn

# Async database initialization
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Isekai Habit API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend origins (change this in production!)
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Include routes
app.include_router(router)

# Startup event to initialize DB
@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
def home():
    return {"message": "Welcome to Isekai Habit API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
