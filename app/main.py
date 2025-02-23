from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router  # Use 'app.routes' instead of just 'routes'

app = FastAPI(title="Isekai Habit API")

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend origins (change this in production!)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to Isekai Habit API"}
