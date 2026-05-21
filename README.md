# Snake Ladder Game

## Overview
The Snake Ladder Game is a simple web-based multiplayer board game that allows users to play the classic game of Snakes and Ladders. Players will take turns rolling a die and moving their tokens on a 10x10 grid.

## Features
- Create or join game sessions
- Roll a die to move tokens
- Display of snakes and ladders
- Player positions tracking
- Basic chat functionality

## Technology Stack
- **Backend**: Python with FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **WebSocket**: For real-time updates

## Getting Started
1. Clone the repository.
2. Install the required dependencies.
3. Run the backend server.
4. Open the frontend in a web browser.

## API Endpoints
- `POST /api/games`: Create a new game session
- `POST /api/games/join`: Join an existing game session
- `POST /api/games/{gameId}/roll`: Roll the die
- `GET /api/games/{gameId}`: Get current game state
- `POST /api/games/{gameId}/chat`: Send a chat message

## License
This project is licensed under the MIT License.