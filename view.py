def get_name():
    with open('file.txt', 'r') as f:
        return str(f.readline()[1:2]) # пока не поняла, верно ли писать так

def get_number():
    with open('file.txt', 'r') as f:
        return str(f.readline()[2:3])

def what_to_do():
    with open('file.txt', 'r') as f:
        return str(f.readline()[3:])


