import { Route, Routes, BrowserRouter } from "react-router-dom";
import { useState } from "react";
import Signup from "./Pages/SignUp";
import Login from "./Pages/LogIn";
import Game from "./Pages/Game";
import NotFound from "./Pages/NotFound";
import Home from "./Pages/Home";
import APPCONTEXT from "./Context/AppContext.JSX";

function App() {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(null);

    return (
        <APPCONTEXT.Provider value={{ user, setUser, token, setToken }}>
            <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/login" element={<Login />} />
                <Route path="/game" element={<Game />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
            </BrowserRouter>
        </APPCONTEXT.Provider>
    );
}

export default App;