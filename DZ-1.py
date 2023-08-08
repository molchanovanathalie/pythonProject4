# Напишите функцию для транспонирования матрицы Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def re_list(my_list):
     rez_out = []
     length = len(my_list[0])
     i = 0
     while i < length:
         rez = []
         rez.append(my_list[0][i])
         rez.append(my_list[1][i])
         rez_out.append(rez)
         i=i+1
     return rez_out
a = [[1, 2, 3], [4, 5, 6]]
print(re_list(a))