from common_layer.database_models import Question


class TestQuestions:


    def test_prepare_for_database(self):
        question: Question = Question('mock_comp_id', 'mock_question', [{'mock_answer':False}, {'mock_answer':True}],
                                      'mock_explanation', 2, 6)

        question_for_database: dict = question.prepare_for_database()

        assert question_for_database.get('comp_id') == 'mock_comp_id'
        assert question_for_database.get('question') == 'mock_question'
        assert question_for_database.get('answer_0') == {'mock_answer':False}
        assert question_for_database.get('answer_1') == {'mock_answer':True}
        assert question_for_database.get('explanation') == 'mock_explanation'
        assert question_for_database.get('difficulty') == 2
        assert question_for_database.get('random') == 6



