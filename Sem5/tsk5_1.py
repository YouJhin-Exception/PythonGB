#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

with open('text_5_1.txt', 'w', encoding='UTF-8') as my_f:
    my_f.write(input('Введите текст для чистки-> '))
with open('text_5_1.txt', 'r',encoding='UTF-8') as my_f:
    some_text = my_f.readline()
    spl_text = some_text.split()

print(some_text, spl_text, sep='\n')

del_smv = input('Введите набор символов для удаления-> ')

def del_some(del_smv):
    fnl_text = " ".join(filter(lambda s: del_smv not in s,spl_text))
    with open('final_text_5_1.txt', 'w', encoding='UTF-8') as my_f:
        my_f.write(fnl_text)
        print(fnl_text)

del_some(del_smv)


# решение преподователя

# from random import sample



# def lst_rnd (count, sim = "абв"):
#     w_lst = []
#     for _ in range (count):
#         lt = sample(sim,3)     #собираем самплом случайное слово из 3 елементов из sim = абв
#         w_lst.append("".join(lt))
#     return " ".join(w_lst)


# # def list_rand_words(count: int, alp: str = 'абв'):
# #     return " ".join("".join(sample(alp, 3)) for _ in range(count)) - укороченная запись

# def simple_sentence(words: str) -> str:
#     #return " ".join(words.replace("абв", "").split())
#     return " ".join(filter(lambda s: "абв" not in s, words.split()))  # через filter

# rnd_words = lst_rnd(int(input("Сколько абв-> ")))
# print(rnd_words)
# print(simple_sentence(rnd_words))



