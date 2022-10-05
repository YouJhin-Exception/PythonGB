from random import sample

n = int(input("Введите длинну списка - "))


def create_rnd_list(n):
    if n < 0:
        print('Длинна списка должна быть больше 0')
        return []
    rnd_list = sample(range(1, n*2), n)
    return rnd_list


def pro_Izi(rnd_list: list):
    print(rnd_list)
    proList = []

    for i in range(len(rnd_list)//2):
        proList.append(rnd_list[i] * rnd_list[len(rnd_list) - 1 - i])

    if len(rnd_list) % 2:
        proList.append(rnd_list[len(rnd_list)//2])

    print(proList)


pro_Izi(create_rnd_list(n))
