import number_chek



def start():
    print('Телефонная книга v.1.0\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_book = '0. Создать новую книгу или очистить существующую'
    new_contact = '1. Добавить новый контакт'
    change_number = '2. Изменить номер телефона'
    change_surname = '3. Изменить фамилию'
    delete_contact = '4. Удалить контакт'
    view_all_contact = '5. Показать все контакты'
    export_to_file_txt = '6. Экспортировать контакты в файл - (txt)'
    export_to_file_csv = '7. Экспортировать контакты в файл - (csv)'
    import_file = '8. Импортировать контакты - (txt)'
    to_exit = '9. Выход'
    print(
        f'{what_to_do}\n\n{new_book}\n{new_contact}\n{change_number}\n{change_surname}\n{delete_contact}\n{view_all_contact}\n{export_to_file_txt}\n{export_to_file_csv}\n{import_file}\n{to_exit}')
    return number_chek.num_chek()
