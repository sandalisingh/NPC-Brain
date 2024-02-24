import React, { useState } from 'react';

function Slider() {
    const [sliderValue, setSliderValue] = useState(0); // State to store the slider value

    // Function to handle change in slider value
    const handleSliderChange = (event) => {
        setSliderValue(parseInt(event.target.value)); // Update the slider value
    };

    return (
        <div>
            {/* Display the current value of the slider */}
            <p>Emotional Value: {sliderValue}</p>
            {/* Display the slider with its current value */}
            <input
                type="range"
                min="0"
                max="10"
                value={sliderValue}
                onChange={handleSliderChange}
                style={{ width: "300px" }} // Optional: Set the width of the slider
            />
        </div>
    );
}

export default Slider;
