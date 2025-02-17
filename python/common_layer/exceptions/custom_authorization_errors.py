

class UnAuthorizedDeleteException(Exception):
    """Exception thrown when we are unauthorized to delete something"""

    def __init__(self, message):
        super().__init__(message)

class UnAuthorizedRequestException(Exception):
    """Exception thrown when an unauthorized request is made"""

    def __init__(self, message):
        super().__init__(message)