# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n //= i
       i += 1
   if n > 1:
       primfac.append(n)
   return primfac


print(primfacs(int(input("Введите число N - "))))

