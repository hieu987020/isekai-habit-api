from fastapi import APIRouter
from datetime import datetime, timedelta
import random
import uuid

router = APIRouter()

@router.get("/habits")
def get_habits():
    today = datetime.now()
    start_date = today - timedelta(days=365)

    # Ensure the start date is a Monday
    while start_date.weekday() != 0:
        start_date -= timedelta(days=1)

    # ✅ Fake user
    user = {
        "user_id": str(uuid.uuid4()),  # ✅ String user ID
        "user_name": "Alice"
    }

    # ✅ Fake habits for the user
    habit_names = ["Workout", "Reading", "Meditation"]
    user_habits = []

    for habit_name in habit_names:
        timeline = {}
        current_date = start_date

        while current_date <= today:
            timeline[current_date.strftime("%Y-%m-%d")] = random.choice([True, False])
            current_date += timedelta(days=1)

        user_habits.append({
            "habit_id": str(uuid.uuid4()),  # ✅ String habit ID
            "habit_name": habit_name,       # ✅ Updated field name
            "timeline": timeline
        })

    # ✅ Return user + habits in correct format
    return {
        "user_id": user["user_id"],
        "user_name": user["user_name"],
        "habits": user_habits
    }
