# x = float(input('Введите число - '))

# как объясняли на семинаре

# y = int(x * 10 ** (len(str(x))-2))
sum = 0
# while(y>0):
#     sum += y%10
#     y = y// 10
# print(sum)

#2e решение
x = input('Введите число - ') 
for i in x:
    if i !=".":
        sum = sum + int(i)

print(sum)
