# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
#       Задача - сформировать файл, содержащий сумму многочленов.

# with open('poly_1.txt', 'w', encoding='utf-8') as file1:
#     file1.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file2:
#     file2.write('23*x^4 + 9*x^6')



def sum_file(file1, file2):
    with open('poly_1.txt', 'r', encoding="utf-8") as f1:
         poly_1 = f1.readlines()
    with open('poly_2.txt', 'r', encoding="utf-8") as f2:
         poly_2 = f2.readlines()

    if len(poly_1) == len(poly_2):
        with open('sum', 'a', encoding="utf-8") as sum_f:
            for i, v in enumerate(poly_1):
                 sum_f.write(f"{v[:-5]} + {poly_2[i]}")
             
    else:
            print("Разное содержимое фаилов")

sum_file("poly_1.txt", "poly_2.txt")
