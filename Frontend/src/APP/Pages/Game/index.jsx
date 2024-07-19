import APPCONTEXT from '../../Context/AppContext.JSX';
import axios from "axios";
import { useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Board from "./Board"

function Game() {
  const { user, token } = useContext(APPCONTEXT);
  const navigate = useNavigate();
  const [board, setBoard] = useState([]);

  console.log(board);

  useEffect(() => {
    if (!user || !token) {
      navigate("/");
      return;
    }
    getboard();
  }, []);
  
  const getboard = () => {
    axios({
      method: "GET",
      url: "http://127.0.0.1:9000/game/board",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((res) => {
      setBoard(res?.data?.board || []);
    })
    .catch((err) => {
      if (!user ||!token) {
        navigate("/");
        return;
      }
    });
  };

  return (
    <div>
      <div className="game-screen">
        <div className="message-panel">
          <p className="welcome-message">Welcome Player: {user?.user_name} </p>
          <div className="button-group">
            <button className="logout-button">Logout</button>
            <button className="new-game-button">New Game</button>
          </div>
        </div>
      </div>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <Board board={board} setBoard={setBoard} getboard={getboard} />
      </div>
    </div>
  );
  
}

export default Game;
