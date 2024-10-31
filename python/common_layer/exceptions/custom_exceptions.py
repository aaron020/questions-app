

class InvalidLambdaInputException(Exception):
    """Exception thrown when the input to lambda is incorrect"""
    def __init__(self, message):
        super().__init__(message)


class DatabaseFailedToAddExeception(Exception):
    """Exception thrown when we fail to add to database"""

    def __init__(self, message):
        super().__init__(message)


