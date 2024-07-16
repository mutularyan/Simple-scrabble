import React from 'react';

function Game() {
  return (
    <div className="game-screen">
      <div className="message-panel">
        <p className="welcome-message">Welcome Player: //user name</p>
        <div className="button-group">
          <button className="logout-button">Logout</button>
          <button className="new-game-button">New Game</button>
        </div>
      </div>
    </div>
  );
}

export default Game;
