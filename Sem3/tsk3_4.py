from random import sample, uniform

n = int(input("Введите длинну списка - "))


def create_rnd_list(n):
    rnd_list = []
    if n < 0:
        print('Длинна списка должна быть больше 0')
        return []
    for i in range(n):
        rnd_list.append(round(uniform(1, n), 2))
    return rnd_list


def dif(rnd_list):
    seq_dif = []
    for i in range(len(rnd_list)):
        seq_dif.append(rnd_list[i] % 1)
    return max(seq_dif) - min(seq_dif)


tstL = create_rnd_list(n)
print(tstL)
print(round(dif(tstL), 2))


# sample(round(uniform(1,n),2) ,n)
# round()
# range(a,b)
# uniform(1,n)

#round(uniform(1, n), 2)
