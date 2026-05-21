from fastapi import APIRouter
from services.player_service import PlayerService

router = APIRouter()
service = PlayerService()

# Additional player-related routes can be added here.