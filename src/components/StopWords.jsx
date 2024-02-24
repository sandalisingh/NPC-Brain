import React from 'react';
import { removeStopwords } from 'stopword';

class StopWords extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: "Your input text here...",
            filteredText: "",
            tokens: []
        };
    }

    handleChange = (event) => {
        this.setState({ text: event.target.value });
    };

    performSentimentAnalysis = () => {
        const text = this.state.text;
        // Remove stopwords
        const filteredText = removeStopwords(text.split(' ')).join(' ');
        // Tokenize filtered text
        const tokens = filteredText.split(/\s+/).filter(token => token.trim() !== '');
        this.setState({ filteredText, tokens });
        // You can continue with your sentiment analysis here
    };

    render() {
        return (
            <div>
                <textarea
                    value={this.state.text}
                    onChange={this.handleChange}
                    placeholder="Enter your text here..."
                    rows="6"
                    cols="50"
                />
                <br />
                <button onClick={this.performSentimentAnalysis}>Analyze Sentiment</button>
                <div>
                    <h2>Filtered Text (without stopwords):</h2>
                    <p>{this.state.filteredText}</p>
                    <h2>Tokens:</h2>
                    <ul>
                        {this.state.tokens.map((token, index) => (
                            <li key={index}>{token}</li>
                        ))}
                    </ul>
                </div>
            </div>
        );
    }
}

export default StopWords;
