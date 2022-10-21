import json
import management

path = 'db.json'


def export_txt():
    with open(path, 'r', encoding='UTF-8') as f_1:
        data = json.load(f_1)
        with open('Exp_file_con.txt', 'w') as file:
            for i in range(0, len(data)):
                file.write("".join(data[i]['Name']) + ':' + "".join(data[i]['Surname']) + ':' + "".join(
                    data[i]['Phone_number']) + ':' + "".join(data[i]['Comment'] + '\n'))

    print('Контакты успешно экспортированны\n')
    management.u_choice()


def export_csv():
    with open(path, 'r', encoding='UTF-8') as f_1:
        data = json.load(f_1)
        with open('Exp_file_csv.csv', 'w') as file:
            for i in range(0, len(data)):
                file.write("".join(data[i]['Name']) + ':' + "".join(data[i]['Surname']) + ':' + "".join(
                    data[i]['Phone_number']) + ':' + "".join(data[i]['Comment'] + '\n'))

    print('Контакты успешно экспортированны\n')
    management.u_choice()

