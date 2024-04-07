// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // Importing the App component
import './index.css'; // Global styles

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
