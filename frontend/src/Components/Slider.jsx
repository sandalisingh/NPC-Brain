import React, { useState } from 'react';
import '../App.css';

function Slider({ onPersonalityVectorChange }) {
    const SliderNames = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'];

    const [slider_vector, setSliderVector] = useState([0, 0, 0, 0, 0]); // State to store the names, values, and options of sliders

    // Function to handle change in slider value
    const handleSliderChange = (index, event) => {
        const newSliders = [...slider_vector];
        newSliders[index] = parseInt(event.target.value);
        setSliderVector(newSliders);
        onPersonalityVectorChange(newSliders);
    };

    return (
        <div className='MediumText SliderBox'>
            <div className='Line'></div>
            <p>
                Craft your character's personality<br />
            </p>
            <div className='Line'></div>
            {slider_vector.map((slider, index) => (
                <div key={index}>
                    <p>{SliderNames[index]}
                        <input
                            className='Slider'
                            type="range"
                            min="0"
                            max="10"
                            value={slider}
                            onChange={(event) => handleSliderChange(index, event)}
                        />{slider}</p>
                </div>
            ))}
            <div className='Line'></div>
        </div>
    );
}

export default Slider;
