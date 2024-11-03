import logo from './logo.svg';
import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { QuestionEntry } from './components/QuestionEntry';
import { QuestionDisplay } from './components/QuestionDisplay'
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <div>
        <Routes>
          <Route path="/" element={<QuestionEntry />} />
          <Route path="/view" element={<QuestionDisplay />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
