import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
    return (
        <div>
            <h1>Welcome to My Game</h1>
            <div className="button-class">
                <Link to="/signup">
                    <button className="button">Sign Up</button>
                </Link>
            </div>
            <div className="button-class">
                <Link to="/login">
                    <button className="button">Login</button>
                </Link>
            </div>
            <div className="button-class">
                <Link to="/game">
                    <button className="button">Play Game</button>
                </Link>
            </div>
        </div>
    );
}

export default Home;