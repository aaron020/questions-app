from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict


@dataclass
class Question:
    question_id: Optional[str] = None
    topic_id: Optional[str] = None
    question: Optional[str] = None
    answers: Optional[List[Dict[str,bool]]] = field(default_factory=list)
    explanation: Optional[str] = None
    difficulty: Optional[int] = None
    random: Optional[int] = None
    user_id: Optional[str] = None

    def prepare_for_database(self) -> dict:
        question_for_database = {'question_id': self.question_id, 'topic_id': self.topic_id, 'questions': self.question,
                                 'explanation': self.explanation,
                                 'difficulty': self.difficulty, 'random': self.random, 'user_id': self.user_id}
        for answer_index in range(len(self.answers)):
            question_for_database[f'answer_{answer_index}'] = self.answers[answer_index]
        return question_for_database


