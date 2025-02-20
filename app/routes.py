from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/habits")
def get_habits():
    today = datetime.now()
    start_date = today - timedelta(days=365)

    # Ensure the start date is a Monday
    while start_date.weekday() != 0:
        start_date -= timedelta(days=1)

    habits = []
    current_date = start_date
    while current_date <= today:
        habits.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "completed": bool(current_date.day % 2)  # Example: Alternating days
        })
        current_date += timedelta(days=1)

    return {"habits": habits}
