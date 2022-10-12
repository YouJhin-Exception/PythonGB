# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.
from itertools import groupby
from os import path

with open('RLE_in.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))

with open('RLE_in.txt', 'r') as file:
    in_text = file.readline()
    
def rle_encode(text):
    
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

print(rle_encode(in_text))

with open('RLE_out.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(rle_encode(in_text))


with open('RLE_out.txt', 'r') as file:
    in_text = file.readline()

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

print(decoding(in_text))

with open('RLE_decode.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(decoding(in_text))


#------------------------------------------------------
#Решение преподователя (разобрать!!!)




# def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
#     if path.exists(text) and path.exists(code_text):
#         with open(text) as my_f_1, \
#                 open(code_text, "a") as my_f_2:
#             for i in my_f_1:
#                 my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
#     else:
#         print("The files do not exist in the system!")


# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             n = ""
#             for k in my_f:
#                 word_nums = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         n += i
#                     else:
#                         word_nums.append([int(n), i])
#                         n = ""
#                 print("".join(starmap(lambda x, y: x * y, word_nums)))
#     else:
#         print("The files do not exist in the system!")

# # def rle_decode(name):
# #     if path.exists(name):
# #         with open(name) as my_f:
# #             for i in my_f:
# #                 word_nums = ["".join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
# #                 print("".join([f"{int(word_nums[i]) * word_nums[i + 1]}" for i in range(0, len(word_nums), 2)]))
# #     else:
# #         print("The files do not exist in the system!")

# # aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
# rle_decode(input("Enter the name of the file to decode: "))





