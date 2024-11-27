from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict


@dataclass
class Question:
    comp_id: Optional[str] = None
    topic: Optional[str] = None
    question: Optional[str] = None
    answers: Optional[List[Dict[str,bool]]] = field(default_factory=list)
    explanation: Optional[str] = None
    difficulty: Optional[int] = None
    random: Optional[int] = None
    user_id: Optional[str] = None

    def prepare_for_database(self) -> dict:
        question_for_database = {'comp_id': self.comp_id, 'topic': self.topic, 'question': self.question,
                                 'explanation': self.explanation,
                                 'difficulty': self.difficulty, 'random': self.random, 'user_id': self.user_id}
        for answer_index in range(len(self.answers)):
            question_for_database[f'answer_{answer_index}'] = self.answers[answer_index]
        return question_for_database


