import random
n = int(input("Введите количество элементов массива - "))
frst_list = []
for i in range(n):
    frst_list.append(i)
print(frst_list)

for i in range(len(frst_list)):
        indxPos = random.randint(0, len(frst_list)-1)
        temp = frst_list[i]
        frst_list[i] = frst_list[indxPos]
        frst_list[indxPos] = temp
print(frst_list)
