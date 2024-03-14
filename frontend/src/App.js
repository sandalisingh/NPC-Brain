import React from 'react';
import './App.css';
import Header from './Components/Header';
import Chat from './Components/Chat';
import NPC from './Components/NPC';

function App() {
  return (
    <div className="App">
      <Header />
      <NPC />
      <Chat />
    </div>
  );
}

export default App;
