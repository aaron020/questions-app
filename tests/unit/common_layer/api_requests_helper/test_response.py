from common_layer.api_requests_helper import Response, StatusCodes


class TestResponse:

    def test_build_response_list(self):
        response = Response(StatusCodes.STATUS_OK, {'header':'hey'}, [{'hey':True},67,'hello']).build_response()

        assert response.get('statusCode') == 200
        assert response.get('headers') == {'header':'hey'}
        assert response.get('body') == '[{"hey": true}, 67, "hello"]'