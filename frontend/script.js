document.getElementById('createGame').addEventListener('click', function() {
    const gameName = document.getElementById('gameName').value;
    fetch('/api/games', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ gameName })
    })
    .then(response => response.json())
    .then(data => alert('Game created with ID: ' + data.gameId));
});

document.getElementById('joinGame').addEventListener('click', function() {
    const gameId = document.getElementById('joinGameId').value;
    const playerName = document.getElementById('playerName').value;
    fetch('/api/games/join', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ gameId, playerName })
    })
    .then(response => response.json())
    .then(data => alert('Joined game as player ID: ' + data.playerId));
});