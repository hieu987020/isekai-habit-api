import os
import logging
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Set the environment (default to 'local' if not specified)
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

# Load the corresponding .env file
if ENVIRONMENT == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env.local")

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get database URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set! Check your environment file.")

logger.info(f"✅ Connecting to database at: {DATABASE_URL}")

# Create async database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session factory
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Define Base model
Base = declarative_base()

# Initialize the database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
