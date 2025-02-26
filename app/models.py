from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    logs = relationship('HabitLog', back_populates='user')  # Fixing relationship

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    logs = relationship('HabitLog', back_populates='habit')  # Fixing relationship

class HabitLog(Base):
    __tablename__ = 'habit_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    habit_id = Column(Integer, ForeignKey('habits.id'))

    user = relationship('User', back_populates='logs')
    habit = relationship('Habit', back_populates='logs')

# Database connection
DATABASE_URL = "postgresql://frieren@localhost/isekai_habit"  # Adjust if needed
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(engine)
