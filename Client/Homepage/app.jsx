// src/App.js
import React, { useState } from 'react';
import './style.css';

function App() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:3000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
      });

      const data = await response.json();

      if (data.success) {
        console.log('Registration successful:', data);
        // Handle success, e.g., redirect to login page
      } else {
        console.error('Error during registration:', data.error);
        // Handle error, e.g., display error message to the user
      }
    } catch (error) {
      console.error('Error during registration:', error);
    }
  };

  return (
    <div className="App">
      <h1>Registration Form</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
        </label>

        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>

        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </label>

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default App;
