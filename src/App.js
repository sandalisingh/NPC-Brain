import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Range from './components/Range';
import Environment from './components/Environment';
import Slider from './components/Slider';
import emotions from './components/emotions'
import SliderComparison from './components/SliderComparison';
import StopWords from './components/StopWords';
import EmotionTagger from './components/EmotionTagger';
// import Lemmatizer from './components/Lemmatizer';

function App() {
  return (
    <div className="App">
      <Header />
      <SearchBar />
      <SliderComparison />
      <EmotionTagger />
    </div>
  );
}

export default App;
