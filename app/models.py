from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    logs = relationship('HabitLog', back_populates='user')

class Habit(Base):
    __tablename__ = 'habits'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    logs = relationship('HabitLog', back_populates='habit')

class HabitLog(Base):
    __tablename__ = 'habit_logs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    habit_id = Column(Integer, ForeignKey('habits.id'))
    user = relationship('User', back_populates='logs')
    habit = relationship('Habit', back_populates='logs')
