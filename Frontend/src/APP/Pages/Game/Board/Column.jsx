import React from 'react';

function Row(props) {
  const { row = [] } = props;

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
            }}
          >
            {letter}
          </div>
        );
      })}
    </div>
  );
}

export default Row;
