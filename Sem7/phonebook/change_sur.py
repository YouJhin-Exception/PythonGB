import json
import management

path = 'db.json'


def change_surname():
    name = input('Введите имя или фамилию контакта для изменения: ')
    with open(path, 'r', encoding='UTF-8') as f_1:
        data = json.load(f_1)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Surname'] = input('Новая фамилия: ')
                with open(path, 'w', encoding='UTF-8') as f_1:
                    json.dump(data, f_1, indent=4)
                print('Фамилия сохранена\n')

    management.u_choice()
