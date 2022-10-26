import menu_chek


def start():
    print('Эллектронный журнал школы №1 v.1.0\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    look_book = '0. Просмотр журнала'
    create_new_db = '1. Создать новую базу'
    add_new = '2. Добавить ученика в журнал'
    change_cl = '3. Изменить класс ученика'
    change_per = '4. Изменить успеваемость'
    del_ch = '5. Удалить запись с журнала'
    to_exit = '6. Выход'
    print(
        f'{what_to_do}\n\n{look_book}\n{create_new_db}\n{add_new}\n{change_cl}\n{change_per}\n{del_ch}\n{to_exit}')
    return menu_chek.num_chek()
