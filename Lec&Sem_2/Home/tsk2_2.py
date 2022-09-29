n = int(input("Введите число N - "))
fkt = 1
for i in range(1, n+1):
    fkt *= i
    print(fkt, end=" ")