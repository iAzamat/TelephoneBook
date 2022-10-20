from argparse import Action


name = ''
phone = ''
action = ''
# t_book = {}


def init(person_name, number):
    global name
    global phone
    global action
    name = person_name
    phone = number
    






def update_note(person_name: str, note: dict, number: str):
    note[person_name] = number
    return note


def delete_note(person_name: str, note: dict):
    del note[person_name]
    return note


def append_number(person_name: str, number: str, note: dict):
    note[person_name].append(number)
    return note


    
    