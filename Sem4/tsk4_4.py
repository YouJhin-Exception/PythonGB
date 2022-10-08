# 4.* Задана натуральная степень n. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

from random import randint
from secrets import choice

def pol(k):
    if k < 1:
        return 0
    
    newPol = ''
    digit = range(0, 10)
    with open("poly_2.txt", "a", encoding="utf-8") as file:
        for i in range(k, 0, -1):
            val = choice(digit)
            if val:
                newPol += f"{val}*x^{i} {choice('+-')}"

        file.write(f"{newPol}{choice(digit)} = 0\n")
            
for _ in range(3):
    pol(int(input("Степень-> ")))
