import React, { useState, useContext } from 'react';
import axios from "axios";
import Error from '../../Components/Error';
import APPCONTEXT from '../../Context/AppContext.JSX';
import { useNavigate } from "react-router-dom";

function Login() {
    const [name, setName] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState(null);
    const { setUser, setToken } = useContext(APPCONTEXT);
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Form submitted:', { name, password });

        axios({
            method: "POST",
            url: "http://127.0.0.1:9000/login", // change this to our backend link
            data: {
              name: name,
              password: password,
            },
          })
            .then((res) => {
              const data = res?.data;
              setToken(data?.token || null);
              setUser(data?.user || null);
              setErrorMessage(null);
              navigate("/game");
            })
            .catch((e) => {
              setErrorMessage(e?.response?.data?.message || "Error: Try Again");
            });
        
    };

    return (
        <div className="login-class">
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-class">
                    <label htmlFor="name">User Name:</label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </div>
                <div className="form-class">
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" className="submit-button">Login</button>
            </form>
            <div>
                <Error errorMessage={errorMessage} />
            </div>
        </div>
    );
}

export default Login;