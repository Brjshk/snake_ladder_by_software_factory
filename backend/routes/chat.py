from fastapi import APIRouter
from services.chat_service import ChatService

router = APIRouter()
service = ChatService()

@router.post('/api/games/{game_id}/chat')
async def send_chat_message(game_id: str, player_id: str, message: str):
    chat_history = service.send_message(game_id, player_id, message)
    return {'chat': chat_history}