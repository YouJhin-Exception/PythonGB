import json
from os import path
import management

filename = 'Exp_file_con.txt'


def import_file(import_f='some.txt'):
    dict1 = []
    with open(import_f) as f_in:
        for line in f_in:
            name, surname, phone_numb, comment = line.strip().split(':')
            dict1.append({'Name': name, 'Surname': surname, 'Phone_number': phone_numb, 'Comment': comment})
    with open('db.json', 'w') as f_db:             # c 'a' дозапись ломается бд, нужно удалить скобки в конце
        json.dump(dict1,f_db,indent=2, ensure_ascii=False)
        print('БД успешно импортированна\n')

    management.u_choice()








