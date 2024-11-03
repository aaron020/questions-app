from common_layer.api_requests_helper import get_response_headers_cors, StatusCodes, Response


def lambda_handler(event, context):
    headers = get_response_headers_cors(allow_methods=['OPTIONS', 'POST', 'GET'])
    return Response(StatusCodes.STATUS_OK, headers, 'preflight request allowed').build_response()