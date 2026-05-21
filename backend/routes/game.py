from fastapi import APIRouter, HTTPException
from services.game_service import GameService

router = APIRouter()
service = GameService()

@router.post('/api/games')
async def create_game(game_name: str):
    game_id = service.create_game(game_name)
    return {'gameId': game_id}

@router.post('/api/games/join')
async def join_game(game_id: str, player_name: str):
    player_id = service.join_game(game_id, player_name)
    return {'playerId': player_id}

@router.post('/api/games/{game_id}/roll')
async def roll_die(game_id: str, player_id: str):
    new_position, game_state = service.roll_die(game_id, player_id)
    return {'newPosition': new_position, 'gameState': game_state}

@router.get('/api/games/{game_id}')
async def get_game_state(game_id: str):
    game_state = service.get_game_state(game_id)
    return game_state