import React, { useState } from 'react';
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Error from '../../Components/Error';

function Signup() {
    const [alias, setAlias] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState(null);
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Form submitted:', { alias, email, password });
        
        axios({
            method: "POST",
            url: "http://127.0.0.1:9000/signup", 
            data: {
              alias: alias,
              email: email,
              password: password,
            },
          })
            .then((res) => {
              setErrorMessage(null);
              navigate("/LogIn");
            })
            .catch((e) => {
              setErrorMessage(e?.response?.data?.message || "Error: Try Again");
            });
    };

    return (
        <div className="signup-class">
            <h1>Sign Up</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-class">
                    <label htmlFor="alias">Alias:</label>
                    <input
                        type="text"
                        id="alias"
                        name="alias"
                        value={alias}
                        onChange={(e) => setAlias(e.target.value)}
                        required
                    />
                </div>
                <div className="form-class">
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
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
                <button type="submit" className="submit-button">Register</button>
            </form>
            <div>
                <Error errorMessage={errorMessage} />
            </div>
        </div>
    );
}

export default Signup;
