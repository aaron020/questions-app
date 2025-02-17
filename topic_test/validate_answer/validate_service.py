from common_layer.exceptions import UnAuthorizedRequestException
from database_service import DatabaseService


class ValidateService:

    def __init__(self, database_service: DatabaseService, topic_test_id: str, question_id: str):
        self.database_service = database_service
        self.question_id = question_id

        self.topic_test = self.database_service.get_topic_test(topic_test_id)
        self.question = self.database_service.get_question(question_id)

    def check_and_validate(self, user_id: str, answer_id: str) -> tuple:
        self._validate_request(user_id)
        correct: bool = self._validate_answer(answer_id)
        self._update_topic_test(self.topic_test, correct)
        return correct, self.question

    def _validate_request(self, user_id: str):
        if user_id != self.topic_test.get('user_id'):
            raise UnAuthorizedRequestException('Unauthorized user for topic test')

        for question in self.topic_test.get('unanswered_questions'):
            if self.question_id == question:
                return
        raise UnAuthorizedRequestException('Unauthorized question for topic test')

    def _validate_answer(self, answer_id: str) -> bool:
        for answers in self.question.get('answers'):
            if answers.get('answer_id') == answer_id:
                return answers.get('correct')
        raise UnAuthorizedRequestException('Unauthorized answer_id for question')

    def _update_topic_test(self, topic_test: dict, correct: bool):
        topic_test.get('unanswered_questions').remove(self.question_id)
        if correct:
            topic_test.get('answered_correct').append(self.question_id)
        else:
            topic_test.get('answered_incorrect').append(self.question_id)

        self.database_service.update_topic_test(topic_test)


