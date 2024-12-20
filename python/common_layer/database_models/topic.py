from dataclasses import dataclass
from typing import Optional


@dataclass
class Topic:
    topic_id: Optional[str] = None
    user_id: Optional[str] = None
    topic_name: Optional[str] = None
    description: Optional[str] = None

    def prepare_for_database(self) -> dict:
        return {
            'topic_id': self.topic_id,
            'user_id': self.user_id,
            'topic_name': self.topic_name,
            'description': self.description
        }

    @staticmethod
    def valid_topic_keys() -> list:
        return ['user_id','topic_name', 'description']
