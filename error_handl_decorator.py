def error_handling_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as error:
            error_message = {
                ValueError: "please provide valid value",
                KeyError: "please provide valid input",
                IndexError: "no records found", 
            }.get(type(error))
            
            return(f"{error_message}")
    
    return inner