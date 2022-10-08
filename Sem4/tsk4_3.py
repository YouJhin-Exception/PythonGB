from random import uniform, randrange


# 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности в том же порядке.

def create_rnd_list(n):
    rnd_list = []
    if n < 0:
        print('Длинна списка должна быть больше 0')
        return []
    for i in range(n):
        rnd_list.append(randrange(n))
    return rnd_list


seqList = create_rnd_list(int(input("Введите длинну списка -> ")))
print(seqList)


def uniqList(list):
    uniqElemList = [i for i in list if list.count(i) == 1] #помещаем в список если элемент только 1
    return uniqElemList

print(uniqList(seqList))