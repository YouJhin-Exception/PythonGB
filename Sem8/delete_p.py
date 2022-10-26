import csv
import mana_t as mt


def del_p():
    count = 0
    print('Для удаления записи введите Фамилию и Имя учащегося')
    surename = input('Введите фамилию -> ')
    name = input('Введите Имя -> ')
    with open('db.csv', 'r', encoding='UTF-8') as f_1, open("tempDB.csv", mode="w", encoding='utf-8') as out_f:
        writer = csv.writer(out_f, delimiter=",", lineterminator="\r")
        for row in csv.reader(f_1):
            if row[0].isalpha():
                writer.writerow(row)
            if row[1] != surename and row[2] != name and row[0].isdigit():
                row[0] = count + 1
                writer.writerow(row)
                count += 1
    with open('tempDB.csv', 'r', encoding='UTF-8') as f_2,  open("db.csv", mode="w", encoding='utf-8') as out_f2:
        writer = csv.writer(out_f2, delimiter=",", lineterminator="\r")
        for row in csv.reader(f_2):
            writer.writerow(row)
    print('Запись удалена\n')
    mt.u_choice()

# del_p()
