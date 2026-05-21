from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)
    name = Column(String, nullable=False)
    position = Column(Integer, default=0)
