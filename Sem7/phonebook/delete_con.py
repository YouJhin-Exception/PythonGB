import json
import management

path = 'db.json'


def del_con():
    name = input('Введите имя или фамилию контакта для удаления: ')
    with open(path, 'r', encoding='UTF-8') as f_1:
        data = json.load(f_1)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
    with open(path, 'w', encoding='UTF-8') as f_1:
        json.dump(data, f_1, indent=4)
    print('Контакт удален\n')
    management.u_choice()
