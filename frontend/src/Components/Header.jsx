import React, { useState } from 'react';
import Slider from './Slider';
import { IoIosRefresh } from "react-icons/io";
import axios from 'axios';

function Header() {

    const [expanded, setExpanded] = useState(false);
    const [environment, setEnvironment] = useState('');
    const [personality_vector, setPersonalityVector] = useState('');

    const toggleExpand = () => {
        setExpanded(!expanded);
    };

    const handlePersonalityChange = (slider_vector) => {
        setPersonalityVector(slider_vector);
    };

    const handleEnvironment = (event) => {
        setEnvironment(event.target.value);
    }

    const onSubmit = async (event) => {
        console.log("BUTTON CLICKED")

        event.preventDefault();

        let dataToSend = {
            environment : environment,
            personality_vector: personality_vector
        }

        console.log("data send")
        console.log(dataToSend)

        try {
            const response = await axios.post('/initialize', dataToSend); // Replace with actual URL
            console.log('Data sent successfully:', response);
        } catch (error) {
            console.error('Error sending data:', error);
        }

        toggleExpand();
    }

    return (
        <header className={`header ${expanded ? 'Expanded' : ''}`}>
            <input name='environment' value={environment} placeholder='Create scenario' onChange={handleEnvironment}></input>
            {
                expanded === true ?
                    <p>
                        <Slider onPersonalityVectorChange={handlePersonalityChange} />
                        <button type='submit' className='RefreshBtn' onClick={onSubmit}><IoIosRefresh /></button>
                    </p>
                    : null
            }
            <p className='Dash' onClick={toggleExpand}></p>
        </header>
    );
}

export default Header;