import telephone_book as tb
import view

t_book = {}

def writing_down():
    name = view.get_name()
    number = view.get_number()
    action = view. what_to_do()
    if action == 'новый контакт':
        if name[0] not in t_book:
            tb.create_new_list(name, t_book, number)
        tb.create_new_note(name, t_book[name[0]], number)
    elif action == 'смена номера':
        tb.update_note(name, t_book[name[0]], number)
    elif action == 'дополнительный номер':
        tb.append_number(name, number, t_book[name[0]])
    elif action == 'удалить номер':
        tb.delete_note(name, t_book[name[0]])
    view.export_book(t_book)
    

