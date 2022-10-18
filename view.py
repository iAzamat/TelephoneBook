def get_name():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[:1]) # пока не поняла, верно ли писать так

def get_number():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[1:2])

def what_to_do():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[2:])


def export_book(book: dict):
    with open('newfile.txt','a') as newfile:
        for k, v in book.items():
            newfile.write(book[k][v])
            