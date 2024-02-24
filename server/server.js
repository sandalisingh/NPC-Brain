const express = require('express');
const bodyParser = require('body-parser');
const natural = require('natural');

const app = express();
const port = 5000;

// Set up middleware to parse JSON requests
app.use(bodyParser.json());

// Lemmatization function
function lemmatize(text) {
    const tokenizer = new natural.WordTokenizer();
    const tokens = tokenizer.tokenize(text);
    const lemmatizer = new natural.LemmaInflector();
    const lemmatizedTokens = tokens.map(token => lemmatizer.lemmatize(token));
    return lemmatizedTokens.join(' ');
}

// Endpoint to handle lemmatization
app.post('/lemmatize', (req, res) => {
    const text = req.body.text;
    const lemmatizedText = lemmatize(text);
    res.json({ lemmatizedText });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
