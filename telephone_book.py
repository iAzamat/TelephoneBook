name = ''
phone = ''
t_book = {}


def init(a, number, book):
    global name
    global phone
    global t_book
    name = a
    phone = number
    t_book = book


def create_new_note(a: str, note: dict, number: str):
    note[a] = list()
    note[a].append(number)


def create_new_list(a: str, book: dict):
    book[a[0]] = dict()


def update_note(a: str, note: dict, number: str):
    note[a] = number


def delete_note(a: str, note: dict):
    del note[a]


def append_number(a: str, number: str, note: dict):
    note[a].append(number)


    
    