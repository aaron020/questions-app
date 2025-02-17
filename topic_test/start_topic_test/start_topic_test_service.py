import uuid
from common_layer.database_models import TopicTest
from database_service import DatabaseService


class StartTopicTest:

    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    def start_topic_test(self, topic_id: str, user_id: str) -> tuple:
        questions: list = self._get_topic_questions(topic_id)
        question_ids = [question['question_id'] for question in questions]
        topic_test : TopicTest = self._create_new_topic_test(question_ids, user_id, topic_id)
        self._add_topic_test_to_database(topic_test)
        return topic_test.topic_test_id ,questions

    def _get_topic_questions(self, topic_id: str) -> list:
        return self.database_service.get_questions_database(topic_id)

    def _add_topic_test_to_database(self, topic_test: TopicTest):
        self.database_service.add_topic_test_database(topic_test)

    def _create_new_topic_test(self, question_ids: list, user_id: str, topic_id: str) -> TopicTest:
        topic_test_id: str = str(uuid.uuid4())
        return TopicTest(
            topic_test_id=topic_test_id,
            topic_id=topic_id,
            user_id=user_id,
            unanswered_questions=question_ids,
            answered_correct=[],
            answered_incorrect=[]
        )


