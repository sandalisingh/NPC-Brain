import React, { useEffect } from 'react';
// import axios from 'axios';
import "../App.css"
import { MessagesContext } from '../App';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import 'bootstrap/dist/css/bootstrap.min.css';

function NPC() {
    const { messages } = React.useContext(MessagesContext);

    // const fetchData = async () => {
    //     try {
    //         const response = await axios.get('http://127.0.0.1:5000/get_states', {
    //             withCredentials: true
    //         });
    //         // setEmoji(response.data.emoji);
    //         // setAction(response.data.action);
    //     } catch (error) {
    //         console.error('Error sending data:', error);
    //     }
    // };

    useEffect(() => {
        // Update the data whenever messages change
        // fetchData();
    }, [messages]); // Add messages as dependency

    return (
        <Container fluid className="NPC-box">
            <Row>
                <Col lg={6} sm={12}>
                    {messages.length > 0 && messages[messages.length - 1].emoji && (
                        <span role="img" aria-label='emoji' className='Emoji'>{messages[messages.length - 1].emoji}</span>
                    )}
                </Col>
                <Col style={{ display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', alignItems: 'flex-start' }}>
                    <Row>
                        <Col>
                            <ul tyle={{ marginTop: 'auto' }}>
                                {window.outerWidth >= 576 && messages.length > 1 && (
                                    <p className="Orange Bubble">
                                        {messages[messages.length - 2].reply}
                                        {messages[messages.length - 2].reply && (
                                            <br />
                                        )}
                                        {messages[messages.length - 2].action && (
                                            <span>({messages[messages.length - 2].action})</span>
                                        )}
                                    </p>
                                )}
                                {messages.length > 0 && (
                                    <p className="Orange Bubble">
                                        {messages[messages.length - 1].reply && (
                                            <>
                                                {messages[messages.length - 1].reply}
                                                <br />
                                            </>
                                        )}
                                        {messages[messages.length - 1].action && (
                                            <span>({messages[messages.length - 1].action})</span>
                                        )}
                                    </p>
                                )}
                            </ul>
                        </Col>
                    </Row>
                </Col>
            </Row>
        </Container>
    );
}


export default NPC;