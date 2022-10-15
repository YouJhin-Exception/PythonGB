# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.


a = [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]

# 1
# res_1 = [j for i, j in zip(a, a[1:]) if j > i]

# 2
# res_2 = [j for i, j in enumerate(a) if i > 0 and a[i] > a[i - 1]]

#3

res = [a[i] for i in range(1, len(a)) if a[i] > a[i-1]]

print(res)