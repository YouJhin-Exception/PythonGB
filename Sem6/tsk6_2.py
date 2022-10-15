# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

n = int(input("Введите N-> "))
print([el for el in range(20, n+1) if el % 20 == 0 or el % 21 == 0])
