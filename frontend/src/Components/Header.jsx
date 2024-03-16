import React, { useState, useContext } from 'react';
import Slider from './Slider';
import { BsEmojiSunglasses } from "react-icons/bs";
import axios from 'axios';
import { MessagesContext } from '../App';

function Header() {
    const { updateMessages } = useContext(MessagesContext);

    const [expanded, setExpanded] = useState(false);
    const [environment, setEnvironment] = useState('');
    const [personality_vector, setPersonalityVector] = useState([0, 0, 0, 0, 0]);

    const toggleExpand = () => {
        setExpanded(!expanded);
    };

    const handlePersonalityChange = (slider_vector) => {
        setPersonalityVector(slider_vector);
    };

    const handleEnvironment = (event) => {
        setEnvironment(event.target.value);
    }

    const onSubmit = async () => {
        let dataToSend = {
            environment: environment,
            personality_vector: personality_vector
        };

        try {
            const response = await axios.post('http://127.0.0.1:5000/initialize', dataToSend, { withCredentials: true });
            updateMessages(response.data);

            console.log('Response:', response);

            const sessionId = response.data.session_id;
            if (sessionId) {
                localStorage.setItem('session_id', sessionId);
            }
            console.log("SESSION ID")
            console.log(sessionId)

        } catch (error) {
            console.error('Error sending data:', error);
        }

        toggleExpand();
    };

    return (
        <header className={`header ${expanded ? 'Expanded' : ''}`}>
            <input onClick={expanded === false ? toggleExpand : null} name='environment' value={environment} placeholder='Forge the reality !' onChange={handleEnvironment}></input>
            {
                expanded === true ?
                    <div>
                        <Slider onPersonalityVectorChange={handlePersonalityChange} />
                        <div className='Center'>
                            <button type='submit' className='RefreshBtn' onClick={onSubmit}>
                                <BsEmojiSunglasses />
                            </button>
                        </div>
                    </div>
                    : null
            }
            <p className='Dash' onClick={toggleExpand}></p>
        </header>
    );
}

export default Header;