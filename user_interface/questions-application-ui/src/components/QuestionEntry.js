import { Col, Container, Row } from "react-bootstrap";
import { useState } from "react"
import { v4 as uuidv4 } from 'uuid';

export const QuestionEntry = () => {
    const randomUUID = uuidv4();

    const formInitDetials ={
        question_id: randomUUID,
        question_body: '',
        option_1: '',
        option_2: '',
        option_3: '',
        question_answer: 0
    }

    const [formDetails, setFromDetails] = useState(formInitDetials);

    const onFormUpdate = (category, value) => {
        setFromDetails({
            ...formDetails,
            [category]: value
        })
    }

    const options = [
        { value: '', label: 'Select an option' },
        { value: '1', label: 'Option 1' },
        { value: '2', label: 'Option 2' },
        { value: '3', label: 'Option 3' }
      ];

    const addQuestion = (e) => {
        e.preventDefault();
        console.log(formDetails);

        fetch('https://baejbbda5f.execute-api.eu-west-1.amazonaws.com/v1/question', {
            method: 'POST',
            headers: {"content-type": "application/json", "x-amz-docs-region": "eu-west-1"},
            mode: 'cors',
            body: JSON.stringify(formDetails)
        })
    }


    return (
        <section className="question" id="question">
            <Container>
                <Row className="align-items-center">
                    <h2>Enter your question:</h2>
                    <Col sm={12} className="px-1">
                        <p>Enter the question:</p>
                        <input type="text" value={formDetails.question_body} placeholder="Question" onChange={(e) => onFormUpdate('question_body',e.target.value)}/>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Option 1:</p>
                        <input type="text" value={formDetails.option_1} placeholder="Option 1" onChange={(e) => onFormUpdate('option_1',e.target.value)}/>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Option 2:</p>
                        <input type="text" value={formDetails.option_2} placeholder="Option 2" onChange={(e) => onFormUpdate('option_2',e.target.value)}/>
                    </Col>
                    <Col sm={4} className="px-1">
                        <p>Option 3:</p>
                        <input type="text" value={formDetails.option_3} placeholder="Option 3" onChange={(e) => onFormUpdate('option_3',e.target.value)}/>
                    </Col>
                    <Col sm={12} className="px-1">
                        <p>Which option is correct:</p>
                        <select
                        value={formDetails.question_answer}
                        onChange={(e) => onFormUpdate('question_answer', parseInt(e.target.value))}
                        >
                        {options.map((option) => (
                            <option key={option.value} value={option.value}>
                            {option.label}
                            </option>
                        ))}
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