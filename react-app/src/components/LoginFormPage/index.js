import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, NavLink, Redirect } from "react-router-dom";
import './LoginForm.css';

function LoginFormPage() {
  const dispatch = useDispatch();
  const history = useHistory();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    history.push("/recipes")
    if (data) {
      setErrors(data);
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">
        <h1>Sign in to Cookbook</h1>
        <form className="login-form" onSubmit={handleSubmit}>
          <ul>
            {errors.map((error, idx) => (
              <li style={{color:"red"}} key={idx}>{error}</li>
            ))}
          </ul>
          <label>
            Email
            <input
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <label>
            Password
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          <button type="submit">Log In</button>
        </form>
        <NavLink exact to="/signup">New User? Sign Up Instead!</NavLink>
      </div>
    </div>
  );
}

export default LoginFormPage;
