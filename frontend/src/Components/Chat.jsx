import React, { useState } from "react";
import "../App.css"
import axios from 'axios';
import { MessagesContext } from '../App';

function Chat() {
    const { messages, updateMessages } = React.useContext(MessagesContext);

    const [inputValue, setInputValue] = useState('');
    const [inputList, setInputList] = useState([]);

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    const handleKeyDown = async (event) => {
        if (event.key === 'Enter') {

            setInputList(prevList => [...prevList.slice(-1), inputValue]);
            setInputValue('');

            try {
                const headers = {
                    'Content-Type': 'application/json'
                };
    
                // const sessionId = localStorage.getItem('session_id');
                // if (sessionId) {
                //     headers['Cookie'] = `session=${sessionId}`;
                // }
    
                // Send a preflight OPTIONS request to check CORS
                await axios.options('http://127.0.0.1:5000/get_response', {
                    headers: headers,
                    withCredentials: true
                });
    
                const response = await axios.post(
                    'http://127.0.0.1:5000/get_response',
                    { chat: inputValue },
                    {
                        headers: headers,
                        withCredentials: true
                    }
                );

                // console.log("SESSION ID")
                // console.log(sessionId)

                updateMessages(response.data);
                console.log(messages)

            } catch (error) {
                console.error('Error sending data:', error);
            }
        }
    };

    return (
        <div className="BottomRight">
            <div>
                <ul>
                {window.outerWidth >= 576 && inputList.length > 1 && (
                    <div style={{ display: 'block' }} key={0}>
                            <p className="Orange ToRight Bubble" key={0}>{inputList[inputList.length-2]}</p>
                        </div>
                )}
                {inputList.length > 0 && (
                    <div style={{ display: 'block' }} key={1}>
                            <p className="Orange ToRight Bubble" key={1}>{inputList[inputList.length-1]}</p>
                        </div>
                )}
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