def error_handling_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as error:
            error_message = {
                ValueError: "please provide name and phone number divided by space",
                KeyError: "please provide valid name",
                IndexError: "phone book is empty", 
            }.get(type(error))
            
            print(f"{error_message}")
    
    return inner