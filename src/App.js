import React from 'react';
import './App.css';
import SliderComparison from './Components/SliderComparison';
import EmotionTagger from './Components/EmotionTagger';
import Header from './Components/Header';
import SearchBar from './Components/SearchBar';

function App() {
  return (
    <div className="App">
      <Header/>
      <SearchBar/>
      <SliderComparison />
      <EmotionTagger />
    </div>
  );
}

export default App;
