import React, { useState } from 'react';
import EmotionTagger from './EmotionTagger';
import SliderComparison from './SliderComparison';

function Header() {

    const [expanded, setExpanded] = useState(false);

    const toggleExpand = () => {
        setExpanded(!expanded);
    };

    return (
        <header className={`header ${expanded ? 'Expanded' : ''}`}>
            <input placeholder='Create scenario'></input>
            {
                expanded === true ?
                    <p>
                        <SliderComparison />
                        <EmotionTagger />
                    </p>
                    : null
            }
            <p className='Dash' onClick={toggleExpand}></p>
        </header>
    );
}

export default Header;