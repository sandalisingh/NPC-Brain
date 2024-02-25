import React, {useState} from 'react';

function Input() {
    // State variable to hold the input value
    const [inputValue, setInputValue] = useState('');

    // Function to handle input change
    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    // Function to handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        // Do something with the input value, for example, log it
        console.log('Input value:', inputValue);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}> 
                    <input type="text" value={inputValue} onChange={handleInputChange} />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default Input;