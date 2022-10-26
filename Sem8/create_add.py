import csv
import mana_t as mt


def create_db():

    with open('db.csv', 'w', encoding="utf8") as db_f:
        names = ['ID', 'Surname', 'Name', 'Br.Date', 'Class', 'St.Performance']
        file_writer = csv.DictWriter(
            db_f, delimiter=",", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
    print('Новая база созданна\n')
    mt.u_choice()


def add_to_db():
    with open('db.csv', 'r', encoding='utf-8') as f:
        id = sum(1 for _ in f)
        print(id)

    with open("db.csv", mode="a", encoding='utf-8') as w_file:
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        br_date = input('Введите дату рождения: ')
        st_class = input('Класс: ')
        perform = input('Успеваемость: ')
        db_csv = {'ID': id, 'Surname': surname, 'Name': name, 'Br.Date': br_date, 'Class': st_class,
                  'St.Performance': perform}
        names = ['ID', 'Surname', 'Name', 'Br.Date', 'Class', 'St.Performance']
        file_writer = csv.DictWriter(
            w_file, delimiter=",", lineterminator="\r", fieldnames=names,)
        # file_writer.writeheader()
        file_writer.writerow(db_csv)

        print('Ученик добавлен\n')

    mt.u_choice()
# add_to_db()
# create_db()
