from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=True)
    description = Column(String, index=True)
    # completed = Column(Integer, default=0)  # 0 for not completed, 1 for completed
