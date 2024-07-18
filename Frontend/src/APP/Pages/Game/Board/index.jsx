import React from 'react';

const styles = {
  boardContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginTop: '30px',  
  },
  board: {
    display: 'flex',
    flexDirection: 'column',
  },
  row: {
    display: 'flex',
  },
  tile: {
    width: '30px',  
    height: '30px', 
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    border: '1px solid #000',
    fontSize: '14px',
    fontWeight: 'bold',
  }
};

const scrabbleColors = [
  ["#ff0000", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ff0000", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#ff0000"],
  ["#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#ffb6c1", "#fff"],
  ["#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff"],
  ["#add8e6", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#add8e6"],
  ["#fff", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#fff"],
  ["#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff"],
  ["#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff"],
  ["#ff0000", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#ff0000"],
  ["#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff"],
  ["#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff"],
  ["#fff", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#fff"],
  ["#add8e6", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#add8e6"],
  ["#fff", "#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ffb6c1", "#fff", "#fff"],
  ["#fff", "#ffb6c1", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#0000ff", "#fff", "#fff", "#fff", "#ffb6c1", "#fff"],
  ["#ff0000", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#fff", "#ff0000", "#fff", "#fff", "#fff", "#add8e6", "#fff", "#fff", "#ff0000"]
];

function Board(props) {
  const { board = [] } = props;

  return (
    <div style={styles.boardContainer}>
      <div style={styles.board}>
        {board.map((row, i) => {
          return <Row key={i} row={row} rowIndex={i} />;
        })}
      </div>
    </div>
  );
}

function Row(props) {
  const { row = [], rowIndex } = props;

  return (
    <div style={styles.row}>
      {row.map((col, i) => {
        let tileStyle = { ...styles.tile, backgroundColor: "#fff" }; 
        if (scrabbleColors[rowIndex] && scrabbleColors[rowIndex][i]) {
          tileStyle.backgroundColor = scrabbleColors[rowIndex][i];
        }

        return (
          <div 
            className="tile" 
            key={i} 
            style={tileStyle}
          >
            {col}
          </div>
        );
      })}
    </div>
  );
}

export default Board;
