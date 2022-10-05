from random import sample, uniform

n = int(input("Введите длинну списка - "))


def create_rnd_list(n):
    if n < 0:
        print('Длинна списка должна быть больше 0')
        return []
    rnd_list = sample(range(1, n*2), n)
    return rnd_list


def n_sum(rnd_list):
    numb_sum = 0
    for i in range(0, len(rnd_list), 2):
        numb_sum += rnd_list[i]
    return numb_sum

# print(n_sum(create_rnd_list(n)))


listN = create_rnd_list(n)
print(listN)
print(n_sum(listN))
