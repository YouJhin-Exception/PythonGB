# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
from decimal import Decimal

# numb = float(input("Введите число- "))
# acc = float(input("Введите точность- "))


def DecNumber (numb,acc):
    numbA = Decimal(numb)         # почему принимает?
    return numbA.quantize(Decimal(f"{acc}"))           # а тут нет

print(DecNumber(float(input("ВВедите число - ")),float(input("Введите точность - "))))

# number = Decimal("0.444")
# number = number.quantize(Decimal("1.00"))
# print(number)
# number = Decimal("0.555678")
# print(number.quantize(Decimal("1.00")))