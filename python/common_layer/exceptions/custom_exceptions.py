

class InvalidLambdaInputException(Exception):
    """Exception thrown when the input to lambda is incorrect"""
    def __init__(self, message):
        super().__init__(message)


class DatabaseFailedToPutExeception(Exception):
    """Exception thrown when we fail to put in database"""

    def __init__(self, message):
        super().__init__(message)


class DatabaseFailedToQueryExeception(Exception):
    """Exception thrown when we fail to query database"""

    def __init__(self, message):
        super().__init__(message)

class DatabaseFailedToDeleteExeception(Exception):
    """Exception thrown when we fail to delete from the database"""

    def __init__(self, message):
        super().__init__(message)

class DatabaseNoContentException(Exception):
    """Exception thrown when we found no content from database"""

    def __init__(self, message):
        super().__init__(message)


