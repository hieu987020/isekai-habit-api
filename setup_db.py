# setup_db.py
from database import engine  # Import the engine from database.py
from app.models import Base  # Import Base for table creation
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database and tables created successfully.")
    except Exception as e:
        logger.error(f"❌ Failed to create tables: {e}")
