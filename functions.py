from error_handl_decorator import error_handling_decorator

phone_book = {}

#parser
@error_handling_decorator
def parse_input(user_input):
    for request in commands.keys():
        if user_input.startswith(request):
            func = commands[request]
            return func(user_input) #new
    return "please provide a valid command"

#adding or changing the phone number
def add_change (user_input):  #ValueError - name or/and phone not provided 
    name = ' '.join(user_input.split(' ')[1:-1])
    phone = user_input.split(' ')[-1]
    if name and phone:
        phone_book[name] = phone
        if user_input.startswith("add"):
            return("new contact successfuly added")
        elif user_input.startswith("change"):
            return("new contact successfuly changed")
    else:
        raise ValueError

#show the phone of user
def phone (user_input):  #KeyError - name is incorrect or missing  
    name = ' '.join(user_input.split(" ")[1:])
    return(f"{name}'s number is {phone_book[name]}")

#show all name-phone pairs
def show_all(_,): #IndexError - no contacts added
    contacts = []
    for name, phone in phone_book.items():
        contacts.append(f"{name}: {phone}")
    if contacts:
        return '; '.join(contacts)
    else:
        raise IndexError

def hello(_,):
    return("How can I help you?")

commands = {
    "add": add_change,
    "change": add_change,
    "phone": phone,
    "show all": show_all,
    "hello": hello,
}         
