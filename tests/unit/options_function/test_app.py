from options_function.app import lambda_handler


class TestApp:

    def test_lambda_handler(self):
        response: dict = lambda_handler(None,None)

        assert response