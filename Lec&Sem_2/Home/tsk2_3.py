n = int(input("Введите число N - "))
sum = 0
n1_list = []
for i in range(1,n+1):
    n1_list.append(int(round((1 + 1/i) ** i,0)))
    sum+=n1_list[i-1]
print(n1_list)
print(f'Сумма элементов = {sum}')