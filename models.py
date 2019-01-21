from sqlalchemy import Column, String, Integer, DateTime, Enum, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

from datetime import datetime, timedelta


class Puzzle(Base):
  """
  자유게시판 글
  """

  __tablename__ = 'puzzles'

  id = Column(Integer, primary_key=True)
  problem = Column(String)
  answer = Column(String, unique=True)
  level = Column(String)

  def __init__(self, **kwargs):
    Base.__init__(self, **kwargs)

  def to_json(self):
    return {
      'id': self.id,
      'level': self.level,
      'problem': self.problem,
      'answer': self.answer
    }