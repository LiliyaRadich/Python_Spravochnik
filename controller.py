import model
import view


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
            case 6:
                search = view.input_search('Введите элемент для поиска: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакт не найден')
            # case 7:
            #     if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
            #         index = view.input_index('Введите номер удаляемого контакта')
            #         # contact = view.change_contact(pb, index)
            #         model.delete_contact(index)
            case 8:
                return