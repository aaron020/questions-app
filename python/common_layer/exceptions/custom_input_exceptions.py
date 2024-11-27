
class InvalidLambdaInputException(Exception):
    """Exception thrown when the input to lambda is incorrect"""
    def __init__(self, message):
        super().__init__(message)