import React, { useState } from 'react';
import { NlpManager } from 'node-nlp';

const Lemmatizer = () => {
  const [inputText, setInputText] = useState('');
  const [lemmatizedText, setLemmatizedText] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const lemmatizeText = () => {
    const manager = new NlpManager({ languages: ['en'] });
    manager.load()
      .then(() => manager.process('en', inputText))
      .then((response) => {
        const lemmatized = response.utterance;
        setLemmatizedText(lemmatized);
      })
      .catch((err) => console.error(err));
  };

  return (
    <div>
      <textarea
        value={inputText}
        onChange={handleInputChange}
        placeholder="Enter text to lemmatize..."
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={lemmatizeText}>Lemmatize</button>
      <br />
      <div>
        <strong>Lemmatized Text:</strong>
        <p>{lemmatizedText}</p>
      </div>
    </div>
  );
};

export default Lemmatizer;
