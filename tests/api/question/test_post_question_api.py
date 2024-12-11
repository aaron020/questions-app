import pytest
import requests
import os
from dotenv import load_dotenv, dotenv_values

api_url = 'https://jbfutu0890.execute-api.eu-west-1.amazonaws.com/Prod/question'
auth_url = 'https://cognito-idp.eu-west-1.amazonaws.com/'

class TestGetQuestion:

    @pytest.fixture
    def get_headers(self):
        try:
            vars = dotenv_values('../../../.env')
            test_account_pwd = vars['TEST_ACCOUNT_PWD']
        except Exception as e:
            print(e)
        try:
            headers = {
                'Content-Type': 'application/x-amz-json-1.1',
                'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
                'Host': 'cognito-idp.eu-west-1.amazonaws.com'
            }
            body = {
                'AuthFlow': 'USER_PASSWORD_AUTH',
                'AuthParameters': {
                    'USERNAME': 'testing_user',
                    'PASSWORD': test_account_pwd
                },
                'ClientId': '7mf7maqg1j7l98rouhjlisomvr'
            }
            response = requests.post(url=auth_url,json=body, headers=headers)
            data = response.json()
            id_token = data.get('AuthenticationResult').get('IdToken')

            return {
                'x-amz-docs-region': 'eu-west-1',
                'Authorization': f'Bearer {id_token}'
            }
        except requests.exceptions.RequestException as e:
            print('Error:', e)

    def test_post_question_200(self, get_headers):
        question_body = {
            'question': 'What is and max retention period for messages in a queue?',
            'answers': [{'4 days default, 10 days max': True}, {'4 days default, 10 days max': False}],
            'topic': 'test',
            'explanation': 'Im not really sure',
            'difficulty': 2
        }

        try:
            response = requests.post(
                url=api_url,
                json=question_body,
                headers=get_headers
            )
            assert response.status_code == 200
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            assert False

