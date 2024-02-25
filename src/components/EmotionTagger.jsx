import React, { useState } from 'react';
// import * as use from '@tensorflow-models/universal-sentence-encoder';
import './EmotionTagger.css';
import { IoRefreshCircleOutline } from "react-icons/io5";
import tag_emotions from '../../scripts/EmotionClassifier' 

// Define a basic list of stopwords
const stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'];

const EmotionTagger = () => {
    const [text, setText] = useState('');
    const [emotionTags, setEmotionTags] = useState({});
    const [finalEmotion, setFinalEmotion] = useState({ name: '', value: '' });
    const [initialEmotion, setInitialEmotion] = useState('');
    const [initialEmoji, setInitialEmoji] = useState('');
    const [finalEmoji, setFinalEmoji] = useState('');
    const [perception, setPerception] = useState('');

    const handleTextChange = (e) => {
        setText(e.target.value);
    };

    const handleInitialEmotionChange = (e) => {
        setInitialEmotion(e.target.value);
        setInitialEmoji(getEmoji(e.target.value));
    };

    const tagEmotions = async () => {

        // Tokenize the input text and remove stopwords
        const tokens = preprocessText(text);

        // Example: Mock emotion prediction (random for demonstration)
        const predictedEmotions = tokens.map(() => {
            const emotions = ['loving', 'confident', 'excited', 'annoyed', 'teasing', 'sad', 'happy', 'angry', 'nervous', 'crying'];
            return emotions[Math.floor(Math.random() * emotions.length)];
        });

        // Calculate the final emotion based on initial emotion
        const finalEmotionBasedOnInitial = calculateFinalEmotionBasedOnInitial(initialEmotion, predictedEmotions);
        const finalEmoji = getEmoji(finalEmotionBasedOnInitial.name);
        const perception = getPerception(finalEmotionBasedOnInitial.name);

        // Create a mapping of tokens to predicted emotions
        const taggedEmotions = {};
        tokens.forEach((token, idx) => {
            if (!taggedEmotions[token]) {
                taggedEmotions[token] = [];
            }
            taggedEmotions[token].push(predictedEmotions[idx]);
        });

        // Update emotion tags state, initial emotion state, final emotion state, and perception state
        setEmotionTags(taggedEmotions);
        setFinalEmotion(finalEmotionBasedOnInitial);
        setFinalEmoji(finalEmoji);
        setPerception(perception);
    };

    // // Function to preprocess text: tokenize and remove stopwords
    // const preprocessText = (text) => {
    //     const tokens = text.toLowerCase().split(/\s+/);
    //     return tokens.filter(token => !stopwords.includes(token));
    // };

    // // Function to calculate the final emotion based on initial emotion
    // const calculateFinalEmotionBasedOnInitial = (initialEmotion, predictedEmotions) => {
    //     if (!initialEmotion) return { name: 'Neutral', value: '0.00' }; // If no initial emotion is provided, return Neutral

    //     // Assign weights for initial emotion and predicted emotions
    //     const initialEmotionWeight = 0.3; // Adjust this weight according to preference
    //     const predictedEmotionWeight = 1 - initialEmotionWeight;

    //     // Calculate the total weight of predicted emotions
    //     const totalPredictedEmotionWeight = predictedEmotionWeight * predictedEmotions.length;

    //     // Calculate the sum of weights for all emotions including initial emotion
    //     const totalWeight = initialEmotionWeight + totalPredictedEmotionWeight;

    //     // Calculate the weighted average of initial emotion and predicted emotions
    //     let weightedSum = 0;
    //     if (predictedEmotions.includes(initialEmotion)) {
    //         // If initial emotion is in predicted emotions, assign a higher weight to it
    //         weightedSum += initialEmotionWeight;
    //     }
    //     for (const emotion of predictedEmotions) {
    //         if (emotion !== initialEmotion) {
    //             weightedSum += predictedEmotionWeight;
    //         }
    //     }

    //     // Calculate the final emotion value based on the weighted sum
    //     const finalEmotionValue = weightedSum / totalWeight;

    //     // Choose the final emotion from the predicted emotions randomly
    //     const filteredPredictedEmotions = predictedEmotions.filter(emotion => emotion !== initialEmotion);
    //     const finalEmotion = filteredPredictedEmotions[Math.floor(Math.random() * filteredPredictedEmotions.length)];

    //     return { name: finalEmotion, value: finalEmotionValue.toFixed(2) };
    // };

    // // Function to get emoji based on emotion
    // const getEmoji = (emotion) => {
    //     switch (emotion) {
    //         case 'loving':
    //             return '😍';
    //         case 'confident':
    //             return '😎';
    //         case 'excited':
    //             return '🤩';
    //         case 'annoyed':
    //             return '😠';
    //         case 'teasing':
    //             return '😜';
    //         case 'sad':
    //             return '😢';
    //         case 'happy':
    //             return '😄';
    //         case 'angry':
    //             return '😡';
    //         case 'nervous':
    //             return '😰';
    //         case 'crying':
    //             return '😭';
    //         default:
    //             return '';
    //     }
    // };

    // // Function to get perception based on emotion
    // const getPerception = (emotion) => {
    //     switch (emotion) {
    //         case 'loving':
    //             return "I feel warmth.";
    //         case 'confident':
    //             return "I am self-assured.";
    //         case 'excited':
    //             return "I'm filled with anticipation.";
    //         case 'annoyed':
    //             return "I'm irritated.";
    //         case 'teasing':
    //             return "I'm playfully bantering.";
    //         case 'sad':
    //             return "I feel sorrow.";
    //         case 'happy':
    //             return "I am joyful.";
    //         case 'angry':
    //             return "I'm frustrated.";
    //         case 'nervous':
    //             return "I'm uneasy.";
    //         case 'crying':
    //             return "I feel sadness.";
    //         default:
    //             return '';
    //     }
    // };

    return (
        <div className='MediumText Center'> 
            <div className='Line'></div>
            <h3>Create your own Environment!</h3>
            <textarea value={text} onChange={handleTextChange} />
            <button className='RefreshBtn' onClick={tagEmotions}><IoRefreshCircleOutline /></button>
            <div>
                {/* Display emotion tags */}
                {Object.entries(emotionTags).map(([token, emotions]) => (
                    <div key={token}>
                        {token}: {emotions.join(', ')}
                    </div>
                ))}
            </div>
            <div>
                <br />
                Perception: {perception}
                <br />
                {/* Display final emotion */}
                Final Emotion: {finalEmotion.name} ({finalEmotion.value})
                {finalEmoji && <span>{finalEmoji}</span>}
                <br />
            </div>
        </div>
    );
};

export default EmotionTagger;
