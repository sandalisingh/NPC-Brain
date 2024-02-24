import React, { Component } from 'react';
import './App.css';
import SliderComparison from './components/SliderComparison';
import EmotionTagger from './components/EmotionTagger';
// import Lemmatizer from './components/Lemmatizer';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
        {/* Openness: <Range /> */}
        {/* Openness: <Slider />
        Conscientiousness: <Slider />
        Extraversion: <Slider />
        Agreeableness: <Slider />
        Neuroticism: <Slider /> */}
        {/* <Environment />
        <StopWords /> */}
        {/* <Lemmatizer /> */}
        <h1>NPC Character Engine</h1>
        <p>Update your NPC's Personality for better game interaction!</p>
      </header>
      <SliderComparison />
      <EmotionTagger />
    </div>
  );
}

export default App;

// import React from 'react';
// import './App.css';
// import EmotionTagger from './components/EmotionTagger';
// import SliderComparison from './components/SliderComparison';

// function App() {
//   return (
//     <div className="container">
//       <div className="header">
//         <h1>Emotion Analyzer</h1>
//         <p>Understand your emotions with AI</p>
//       </div>
//       <SliderComparison />
//       <EmotionTagger />
//     </div>
//   );
// }

// export default App;
