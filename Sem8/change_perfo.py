import csv
import mana_t as mt


def chg_perfo():
    print('Для изменения успеваемости введите Фамилию и Имя учащегося')
    surename = input('Введите фамилию -> ')
    name = input('Введите Имя -> ')
    with open('db.csv', 'r', encoding='UTF-8') as f_1, open("tempDB.csv", mode="w", encoding='utf-8') as out_f:
        writer = csv.writer(out_f, delimiter=",", lineterminator="\r")
        for row in csv.reader(f_1):
            if row[1] != surename and row[2] != name:
                writer.writerow(row)
            if row[1] == surename and row[2] == name:
                row[5] = input('Введите новую успеваемость -> ')
                writer.writerow(row)
    with open('tempDB.csv', 'r', encoding='UTF-8') as f_2,  open("db.csv", mode="w", encoding='utf-8') as out_f2:
        writer = csv.writer(out_f2, delimiter=",", lineterminator="\r")
        for row in csv.reader(f_2):
            writer.writerow(row)
    mt.u_choice()
