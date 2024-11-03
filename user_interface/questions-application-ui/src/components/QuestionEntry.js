import { Col, Container, Row } from "react-bootstrap";
import { useState } from "react"
import { v4 as uuidv4 } from 'uuid';

export const QuestionEntry = () => {

    const formInitDetials ={
        question: '',
        answer_1: '',
        answer_2: '',
        answer_3: '',
        checkbox_1: false,
        checkbox_2: false,
        checkbox_3: false,
        topic: 'aws',
        explanation: '',
        difficulty: 0
    }

    const [formDetails, setFromDetails] = useState(formInitDetials);

    const onFormUpdate = (category, value) => {
        setFromDetails({
            ...formDetails,
            [category]: value
        })
    }

    const addQuestion = (e) => {
        e.preventDefault();
        console.log(formDetails);

        const answers = [
            { [formDetails.answer_1]: formDetails.checkbox_1 },
            { [formDetails.answer_2]: formDetails.checkbox_2 },
            { [formDetails.answer_3]: formDetails.checkbox_3 },
        ];

        const payload = {
            question: formDetails.question,
            answers: answers,
            topic: formDetails.topic,
            explanation: formDetails.explanation,
            difficulty: formDetails.difficulty
        };

        console.log(payload);

        fetch('https://z1rbxkydt4.execute-api.eu-west-1.amazonaws.com/Prod/question', {
            method: 'POST',
            headers: {"content-type": "application/json", "x-amz-docs-region": "eu-west-1"},
            mode: 'cors',
            body: JSON.stringify(payload)
        })
        .then(response => {
            console.log('Raw Response:', response); // Log the raw response
            return response.text(); // Get the response as text first
        })
        .then(text => {
            console.log('Response Text:', text); // Log the response text
            try {
                const data = JSON.parse(text); // Attempt to parse as JSON
                console.log('Parsed Response:', data);
            } catch (error) {
                console.error('JSON Parse Error:', error);
            }
        })
        .catch(error => console.error('Fetch Error:', error));
    }


    return (
        <section className="question" id="question">
            <Container>
                <Row className="align-items-center">
                    <h2>Enter your question:</h2>
                    <Col sm={12} className="px-1">
                        <p>Enter the question:</p>
                        <input type="text" value={formDetails.question} placeholder="Question" onChange={(e) => onFormUpdate('question',e.target.value)}/>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Option 1:</p>
                        <input type="text" value={formDetails.answer_1} placeholder="Answer 1" onChange={(e) => onFormUpdate('answer_1',e.target.value)}/>
                        <div>
                            <input type="checkbox" checked={formDetails.checkbox_1} onChange={(e) => onFormUpdate('checkbox_1', e.target.checked)} />
                            <label>Correct Answer?</label>
                        </div>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Option 2:</p>
                        <input type="text" value={formDetails.answer_2} placeholder="Answer 2" onChange={(e) => onFormUpdate('answer_2',e.target.value)}/>
                        <div>
                            <input type="checkbox" checked={formDetails.checkbox_2} onChange={(e) => onFormUpdate('checkbox_2', e.target.checked)} />
                            <label>Correct Answer?</label>
                        </div>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Option 3:</p>
                        <input type="text" value={formDetails.answer_3} placeholder="Answer 3" onChange={(e) => onFormUpdate('answer_3',e.target.value)}/>
                        <div>
                            <input type="checkbox" checked={formDetails.checkbox_3} onChange={(e) => onFormUpdate('checkbox_3', e.target.checked)} />
                            <label>Correct Answer?</label>
                        </div>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Please Explain:</p>
                        <input type="text" value={formDetails.explanation} placeholder="Explanation" onChange={(e) => onFormUpdate('explanation',e.target.value)}/>
                    </Col>
                    <Col sm={12} className="px-1">
                        <p>Difficulty Level:</p>
                        <select value={formDetails.difficulty} onChange={(e) => onFormUpdate('difficulty', parseInt(e.target.value))}>
                            <option value={0}>Select Difficulty</option>
                            <option value={1}>Easy</option>
                            <option value={2}>Medium</option>
                            <option value={3}>Hard</option>
                        </select>
                    </Col>
                    <Col sm={12} className="px-1">
                        <button onClick={addQuestion}><span>Add Question</span></button>
                    </Col>
                </Row>
            </Container>
        </section>
    );
}