/* eslint-disable react/prop-types */
import React, { useContext } from "react";
import axios from "axios";
import APPCONTEXT from "../../../Context/APPCONTEXT";

function Board(props) {
  const { board = [], setBoard = () => {}, getBoard = () => {} } = props;

  return (
    <div>
      {board.map((row, i) => (
        <Row key={i} r={i} row={row} setBoard={setBoard} getBoard={getBoard} />
      ))}
    </div>
  );
}

function Row(props) {
  const { row = [], r = 0, setBoard = () => {}, getBoard = () => {} } = props;
  const { token } = useContext(APPCONTEXT);

  const handleTileClick = (tile, r, c) => {
    console.log(tile, r, c);

    if (tile.special === "X") {
      axios({
        method: "PUT",
        url: "http://127.0.0.1:9000/game/make-move",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        data: {
          y: r,
          x: c,
        },
      }).then((res) => {
        getBoard();
      });
      return;
    }

    axios({
      method: "GET",
      url: "http://127.0.0.1:9000/game/possible-moves",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (res?.data?.board) {
          setBoard(res?.data?.board);
        }
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div style={{ display: "flex" }}>
      {row.map((tile, colIndex) => {
        const { letter, special } = tile;

        let backgroundColor = "#ffffff";
        let color = "#000000";

        
        switch (special) {
          case "TW":
            backgroundColor = "#ff9800"; 
            break;
          case "DW":
            backgroundColor = "#f44336"; 
            break;
          case "TL":
            backgroundColor = "#03a9f4"; 
            break;
          case "DL":
            backgroundColor = "#4caf50"; 
            break;
          case "X":
            backgroundColor = "#9e9e9e"; 
            break;
          default:
            break;
        }

        return (
          <div
            key={colIndex}
            style={{
              width: "40px",
              height: "40px",
              backgroundColor,
              color,
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              border: "1px solid #000",
              cursor: "pointer",
            }}
            onClick={() => handleTileClick(tile, r, colIndex)}
          >
            <Col value={letter} />
          </div>
        );
      })}
    </div>
  );
}

function Col(props) {
  const { value } = props;

  return (
    <span style={{ fontSize: "24px" }}>
      {value}
    </span>
  );
}

export default Board;
