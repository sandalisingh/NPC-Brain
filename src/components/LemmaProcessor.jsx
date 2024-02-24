// LemmaProcessor.jsx
import natural from 'natural';

const performLemmatization = (text) => {
    const tokenizer = new natural.WordTokenizer();
    const words = tokenizer.tokenize(text);
    const lemmatizer = new natural.LemmaInflector();
    const lemmatizedWords = words.map(word => lemmatizer.lemmatize(word));
    return lemmatizedWords.join(' ');
};

export default performLemmatization;
