from error_handl_decorator import error_handling_decorator
from error_handl_decorator import custom_error
from re import findall


phone_book = {}

#parser
@error_handling_decorator
def parse_input(user_input):
    for request in commands.keys():
        if user_input.startswith(request):
            modif_input = user_input.replace(request, '', 1).strip()
            name = modif_input.split(' ')[0]
            phone = modif_input.split(' ')[-1]
            func = commands[request]
            return func(request, name, phone)
    return "please provide a valid command"

#adding or changing the phone number
def add_change (request, name, phone):  #ValueError - name or/and phone not provided 
    if name and phone:
        phone_book[name] = phone
        if request.startswith("add"):
            return("new contact successfuly added")
        elif request.startswith("change"):
            return("new contact successfuly changed")
    else:
        raise custom_error("please provide name and phone number divided by space")

#show the phone of user
def phone (notused1, name, notused2):  #KeyError - name is incorrect or missing  
    for el in phone_book.keys():
        if name == el:
            return(f"{name}'s number is {phone_book[name]}")
    raise custom_error("please provide valid name")

#show all name-phone pairs
def show_all(notused1, notused2, notused3): #IndexError - no contacts added
    contacts = []
    for name, phone in phone_book.items():
        contacts.append(f"{name}: {phone}")
    if contacts:
        return '; '.join(contacts)
    else:
        raise custom_error("phone book is empty")

def hello(notused1, notused2, notused3):
    return("How can I help you?")

commands = {
    "add": add_change,
    "change": add_change,
    "phone": phone,
    "show all": show_all,
    "hello": hello,
}         
