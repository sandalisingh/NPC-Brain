import React from 'react';
import './App.css';
import Header from './Components/Header';
import Chat from './Components/Chat';
import NPC from './Components/NPC';

function App() {
  var NPC = null;

  const handleInitialization = (environment, personality_vector) => {
  };

  return (
    <div className="App">
      <Header onSubmitInitials={handleInitialization}/>
      <NPC />
      <Chat />
    </div>
  );
}

export default App;
