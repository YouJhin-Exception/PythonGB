import create_add as cr
import view_db as vw
import change_cls as cc
import change_perfo as cp
import delete_p as dp
import ui_menu as ui


def u_choice():
    choice = ui.menu()
    if choice < 0 or choice > 6:
        print('Ошибка!\n Число должно соответсвовать пункту меню\n')
        u_choice()
    elif choice == 0:
        vw.view_all()
    elif choice == 1:
        cr.create_db()
    elif choice == 2:
        cr.add_to_db()
    elif choice == 3:
        cc.chg_cls()
    elif choice == 4:
        cp.chg_perfo()
    elif choice == 5:
        dp.del_p()
    elif choice == 6:
        print('\nЗакрываем журнал')
        exit()
