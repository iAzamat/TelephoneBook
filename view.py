def get_name():
    global name
    with open('file.txt', 'r') as f:
        name = str(f.readlines()[0]) # пока не поняла, верно ли писать так
    return name

def get_number():
    global phone
    with open('file.txt', 'r') as f:
        phone = str(f.readlines()[1])
    return phone

def what_to_do():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[2])


def export_book(book: dict):
    with open('newfile.txt','a') as newfile:
        for k, v in book.items():
            newfile.write(f"{k}, {v}")

def print_dict(book: dict):
    for k, v in book.items():
        print(f"{k}, {v}")