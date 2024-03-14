import React, { useState } from 'react';
import Slider from './Slider';
import { IoIosRefresh } from "react-icons/io";

function Header({onSubmitInitials}) {

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

    const onSubmit = (event) => {
        onSubmitInitials(environment, personality_vector);
        toggleExpand();
    }

    return (
        <header className={`header ${expanded ? 'Expanded' : ''}`}>
            <input name='environment' value={environment} placeholder='Create scenario' onChange={handleEnvironment}></input>
            {
                expanded === true ?
                    <p>
                        <Slider onPersonalityVectorChange={handlePersonalityChange} />
                        <button type='submit' className='RefreshBtn' onSubmit={onSubmit}><IoIosRefresh /></button>
                    </p>
                    : null
            }
            <p className='Dash' onClick={toggleExpand}></p>
        </header>
    );
}

export default Header;