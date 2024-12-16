import requests

api_url = 'https://67xwh4txde.execute-api.eu-west-1.amazonaws.com/Prod/topics/questions'

class TestGetQuestion:

    def test_get_questions_from_database_status_200(self):
        try:
            response = requests.get(f'{api_url}?topic=test')

            assert response.status_code == 200
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            assert False


    def test_get_questions_from_database_status_204(self):
        try:
            response = requests.get(f'{api_url}?topic=test_empty')

            assert response.status_code == 204
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            assert False

    def test_get_questions_from_database_status_400(self):
        try:
            response = requests.get(f'{api_url}?topicer=test_empty')

            assert response.status_code == 400
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            assert False



