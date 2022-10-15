#3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

from os import sep


names =  ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка","маша","дарья","женя"]

# def sort_names (*names):
#     set_names = {name.title() for name in names}
#     f_let = [name[0].upper() for name in set_names]
#     res_dict = {k: list() for k in f_let}

#     for name in names:
        
#         res_dict[name[0]].append(name)

#     return res_dict


#print(sort_names("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))


def sort_names_set(names):

    names_set = dict()
    for name in names:
        ft_let = name[0].upper()
        names_set[ft_let] = names_set.setdefault(ft_let, set()) | {name.capitalize()}
    return names_set
  

print(sort_names_set(names))
