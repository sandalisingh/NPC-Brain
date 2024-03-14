import React, { useState } from "react";
import "../App.css"

function Chat() {
    const [inputValue, setInputValue] = useState('');
    const [inputList, setInputList] = useState([]);

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            setInputList(prevList => [...prevList.slice(-1), inputValue]);
            setInputValue('');
        }
    };

    return (
        <div className="BottomRight">
            <div>
                <ul>
                    {inputList.map((text, index) => (
                        <div style={{display:'block'}}>
                        <li className="Orange" key={index}>{text}</li>
                        </div>
                    ))}
                </ul>
            </div>
            <input
                className="ChatBox Yellow"
                name="chatInput"
                type="text"
                placeholder="|"
                value={inputValue}
                onChange={handleInputChange}
                onKeyDown={handleKeyDown}
                style={{ width: `${Math.max(20, inputValue.length * 10)}px` }}
            />
        </div>
    );
}

export default Chat;