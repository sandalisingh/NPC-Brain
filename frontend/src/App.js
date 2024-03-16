import React, { useState } from 'react';
import './App.css';
import Header from './Components/Header';
import Chat from './Components/Chat';
import NPC from './Components/NPC';

export const MessagesContext = React.createContext({ messages: [], updateMessages: () => { } });

function App() {
  const [messages, setMessages] = useState([]);

  const updateMessages = (newMessage) => {
    setMessages((prevMessages) => {
      // Ensure we keep only the last two messages
      let updatedMessages = [];
      if (prevMessages.length >= 2) {
        updatedMessages = prevMessages.slice(1); // Keep the last message
      } else {
        updatedMessages = [...prevMessages]; // Keep all messages if less than 2
      }
      updatedMessages.push(newMessage); // Add the new message at the end
      console.log("Updated Messages:", updatedMessages);
      return updatedMessages;
    });
  };

  return (
    <MessagesContext.Provider value={{ messages, updateMessages }}>
      <div className="App">
        <Header />
        <NPC />
        <Chat />
      </div>
    </MessagesContext.Provider>
  );
}

export default App;
