export interface QuestionHiddenCorrect {
    question_id: string;
    topic_id: string;
    questions: string;
    answers: AnswerHiddenCorrect[];
    explanation: string;
    difficulty: number;
}

export interface AnswerHiddenCorrect {
    answer: string,
    answer_id: string
}


export interface QuestionWithCorrect {
    question_id: string;
    topic_id: string;
    questions: string;
    answers: AnswerWithCorrect[];
    explanation: string;
    difficulty: number;
}

export interface AnswerWithCorrect {
    answer: string,
    answer_id: string,
    correct: boolean
}
