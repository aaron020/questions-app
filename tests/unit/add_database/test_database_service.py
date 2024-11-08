from add_database.database_service import DatabaseService


class TestDatabaseService:

    def test_convert_to_database_question(self):
        input_question: dict = {
                            'question': 'What is the default and max retention period for messages in a queue?',
                            'answers': [{'4 days default, 10 days max': False}, {'4 days default, 10 days max': True}],
                            'topic': 'aws',
                            'explanation':'Im not really sure',
                            'difficulty':2
                        }

        database_question: dict = DatabaseService(input_question, None).convert_to_database_question(input_question)

        assert database_question.get('topic') == 'aws'
        assert database_question.get('question') == 'What is the default and max retention period for messages in a queue?'
        assert database_question.get('answer_0') ==  {'4 days default, 10 days max': False}
        assert database_question.get('answer_1') == {'4 days default, 10 days max': True}
        assert database_question.get('explanation') == 'Im not really sure'
        assert database_question.get('difficulty') == 2
        assert database_question.get('random') is not None
