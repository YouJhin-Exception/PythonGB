import book_ui as ui
import add_new_con as cr
import change_number as cn
import change_sur as cs
import delete_con as dc
import view_all as va
import export as exp
import import_f as imp


def u_choice():
    choice = ui.menu()
    if choice < 0 or choice > 9:
        print('Ошибка!\n Число должно соответсвовать пункту меню\n')
        u_choice()
    elif choice == 0:
        cr.create_db_json()
    elif choice == 1:
        cr.add_to_db()
    elif choice == 2:
        cn.change_numb()
    elif choice == 3:
        cs.change_surname()
    elif choice == 4:
        dc.del_con()
    elif choice == 5:
        va.view_all_book()
    elif choice == 6:
        exp.export_txt()
    elif choice == 7:
        exp.export_csv()
    elif choice == 8:
        imp.import_file(input('Введите имя фаила-(по умолчанию это-> Exp_file_con.txt <- ->'))
    elif choice == 9:
        print('\nВсего хорошего!')
        exit()
