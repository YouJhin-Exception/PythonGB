n = int(input("Введите для перевода число - "))


def convert_Num(n):
    ls_num = []
    while n > 0:
        ls_num.insert(0, n % 2)
        n //= 2
    print(*ls_num, sep="")


convert_Num(n)
