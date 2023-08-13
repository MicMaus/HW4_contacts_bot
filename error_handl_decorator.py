class custom_error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def error_handling_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except custom_error as ce:
            return str(ce)
    return inner