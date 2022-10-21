import json
import management

path = 'db.json'


def view_all_book():
    with open(path, 'r', encoding='UTF-8') as f_1:
        data = json.load(f_1)
        for i in range(0, len(data)):
            print(data[i])
    management.u_choice()
