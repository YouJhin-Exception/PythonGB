import json
import management


def create_db_json():
    db_json = []
    with open('db.json', 'w') as db_f:
        db_f.write(json.dumps(db_json, indent=2, ensure_ascii=False))
    management.u_choice()


def add_to_db():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    n_phone = input('Введите номер телефона: ')
    comment = input('Комментарий: ')
    db_json = {'Name': name, 'Surname': surname,
               'Phone_number': n_phone, 'Comment': comment}

    data = json.load(open('db.json'))
    data.append(db_json)
    with open('db.json', 'w') as f_db:
        json.dump(data, f_db, indent=2, ensure_ascii=False)
    print('Создан новый контакт\n')
    management.u_choice()
