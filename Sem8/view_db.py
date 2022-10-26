import csv
import mana_t as mt


def view_all():
    with open('db.csv', 'r', encoding='UTF-8') as f_1:
        file_reader = csv.reader(f_1, delimiter=",")
        # for row in file_reader:
        #     print(row)
        count = 0
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                # Вывод строк
                print(
                    f'    {row[0]} - {row[1]} {row[2]} и он родился в {row[3]} году, учится в {row[4]} классе и имеет {row[5]} успеваемость')
            count += 1

    mt.u_choice()
