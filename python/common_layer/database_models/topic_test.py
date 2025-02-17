from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TopicTest:
    topic_test_id: Optional[str] = None
    topic_id: str = None
    user_id: Optional[str] = None
    unanswered_questions: Optional[List] = None
    answered_correct: Optional[List] = None
    answered_incorrect: Optional[List] = None

    def prepare_for_database(self) -> dict:
        return {
            "topic_test_id": self.topic_test_id,
            "topic_id": self.topic_id,
            "user_id": self.user_id,
            "unanswered_questions": self.unanswered_questions,
            "answered_correct": self.answered_correct,
            "answered_incorrect": self.answered_incorrect
        }