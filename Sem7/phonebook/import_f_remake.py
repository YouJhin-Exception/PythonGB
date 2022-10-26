import json
from os import path
import management

filename = 'Exp_file_con.txt'


def import_file(import_f='some.txt'):
    with open(import_f) as f_in, open('db.json') as f_db_r:
        all_data = json.load(f_db_r)

        for line in f_in:
            name, surname, phone_numb, comment = line.strip().split(':')
            all_data.append({'Name': name, 'Surname': surname, 'Phone_number': phone_numb, 'Comment': comment})
        with open('db.json', 'w') as f_db_w:
            json.dump(all_data, f_db_w, indent=2, ensure_ascii=False)
        print('БД успешно импортированна\n')

    management.u_choice()
