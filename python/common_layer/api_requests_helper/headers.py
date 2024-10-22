_DEFAULT_ALLOW_ORIGIN: list = ['*']
_DEFAULT_ALLOW_METHODS: list = ['OPTIONS']
_DEFAULT_ALLOW_HEADERS: list = ['Content-Type','Authorization','X-Amz-Date','X-Api-Key','X-Amz-Security-Token']
_DEFAULT_CONTENT_TYPE: str = 'application/json'

def get_response_headers_cors(allow_origin=None, allow_methods=None, allow_headers=None,
                              content_type=_DEFAULT_CONTENT_TYPE) -> dict:
    allow_origin = allow_origin if allow_origin is not None else _DEFAULT_ALLOW_ORIGIN
    allow_methods = allow_methods if allow_methods is not None else _DEFAULT_ALLOW_METHODS
    allow_headers = allow_headers if allow_headers is not None else _DEFAULT_ALLOW_HEADERS

    return {
        'Access-Control-Allow-Origin': ', '.join(allow_origin),
        'Access-Control-Allow-Methods': ', '.join(allow_methods),
        'Access-Control-Allow-Headers': ', '.join(allow_headers),
        'Content-Type': content_type,
    }