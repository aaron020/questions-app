from common_layer.database_models import Question


class MapQuestion:
    def __init__(self, question_dict: dict):
        self.question_dict: dict = question_dict

    def map_question_dict_to_model_dict(self) -> Question:
        return Question(self.generate_comp_id(),).

    def generate_comp_id(self) -> str: