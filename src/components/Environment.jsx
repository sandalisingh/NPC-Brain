import React, { useState } from 'react';

function InputComponent({ initialValue }) {
    // State variable to hold the input value
    const [inputValue, setInputValue] = useState(initialValue);

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
                <label>
                    Input:
                    <input type="text" value={inputValue} onChange={handleInputChange} />
                </label>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

function Environment() {
    // String value to pass to InputComponent
    const initialValue = "create your own environment";

    return (
        <div>
            <InputComponent initialValue={initialValue} />
        </div>
    );
}

export default Environment;
