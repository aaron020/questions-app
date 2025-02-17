from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict


@dataclass
class Question:
    question_id: Optional[str] = None
    topic_id: Optional[str] = None
    question: Optional[str] = None
    answers: Optional[List] = field(default_factory=list)
    explanation: Optional[str] = None
    difficulty: Optional[int] = None
    random: Optional[int] = None
    user_id: Optional[str] = None

    def prepare_for_database(self) -> dict:
        return {'question_id': self.question_id, 'topic_id': self.topic_id, 'questions': self.question,
                                 'explanation': self.explanation, 'answers': self.answers,
                                 'difficulty': self.difficulty, 'random': self.random, 'user_id': self.user_id}

