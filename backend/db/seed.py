from sqlalchemy.orm import Session
from .models.game import Game
from .models.player import Player
from .models.chat import Chat

def seed_db(db: Session):
    game = Game(name='Sample Game', state={})
    db.add(game)
    db.commit()
    db.refresh(game)

    player1 = Player(game_id=game.id, name='Player 1')
    player2 = Player(game_id=game.id, name='Player 2')
    db.add(player1)
    db.add(player2)
    db.commit()
