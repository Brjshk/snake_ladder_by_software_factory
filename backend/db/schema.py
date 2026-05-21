from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.game import Game
from .models.player import Player
from .models.chat import Chat

DATABASE_URL = 'sqlite:///./snake_ladder_game.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)
