day = int(input("Введите день недели- "))
if day < 1 or day > 7:
    print('Странная у вас неделя...')
elif day == 6 or day == 7:
    print('это выходной день')
else: print('это рабочий день')