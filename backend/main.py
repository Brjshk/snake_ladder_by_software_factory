from fastapi import FastAPI
from routes import game, player, chat

app = FastAPI()

app.include_router(game.router)
app.include_router(player.router)
app.include_router(chat.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)