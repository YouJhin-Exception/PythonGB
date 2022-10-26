
def num_chek():
    try:
        numb = int(input('Введите номер меню: \n'))
        return numb
    except ValueError:
        print('Только число \n')
        return num_chek()
