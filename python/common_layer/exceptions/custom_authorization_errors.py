

class UnAuthorizedDeleteException(Exception):
    """Exception thrown when we are unauthorized to delete something"""

    def __init__(self, message):
        super().__init__(message)
