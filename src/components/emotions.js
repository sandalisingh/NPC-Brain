// Define an array of objects
const emotions = [
    { key: 'Openness', value1: 'Loving', value2: 'Confident' },
    { key: 'Conscientiousness', value1: 'Excited', value2: 'Annoyed' },
    { key: 'Extraversion', value1: 'Teasing', value2: 'Sad' },
    { key: 'Agreeableness', value1: 'Happy', value2: 'Angry' },
    { key: 'Neuroticism', value1: 'Nervous', value2: 'Crying' }
];

// Accessing the list
console.log(emotions[0]); // Output: { key: 'key1', value1: 'value1a', value2: 'value1b' }
console.log(emotions[1]); // Output: { key: 'key2', value1: 'value2a', value2: 'value2b' }

// Iterating through the list
emotions.forEach(item => {
    console.log(item.key, item.value1, item.value2);
});
