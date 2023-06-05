import logging
from functools import wraps


class FridgeCapacityError(Exception):
    """
    Initialize the exception class for the fridge capacity
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


"""
The decorator function that takes the exception and mode as arguments
"""


def logged(exception, mode):
    def decorator(func):
        """
        Preserve the original function's metadata
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                """
                Execute the original function
                """
                return func(*args, **kwargs)
            except exception as e:
                if mode == 'console':
                    """
                    Log the exception to the console
                    """
                    logging.exception(str(e))
                elif mode == 'file':
                    logging.basicConfig(filename='error.log', level=logging.ERROR)
                    """
                    Log the exception to the file
                    """
                    logging.exception(str(e))
                else:
                    """
                    Raise a ValueError if an invalid mode is provided
                    """
                    raise ValueError("Invalid mode. Mode should be 'console' or 'file'.")

        return wrapper

    return decorator
