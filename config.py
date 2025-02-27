import os

is_local = os.getenv("ENV", "local") == "local"

DATABASE_URL = (
    "postgresql://postgres:your_local_password@localhost:5432/isekai_habit"
    if is_local
    else os.getenv("DATABASE_URL")
)
