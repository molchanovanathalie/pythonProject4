# Напишите функцию принимающую на вход только
# ключевые параметры(kwargs) и возвращающую словарь,
# где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не
# хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) ->
# {True: "rev", "YES": 'acc', 4: "stroka"}

def fun_key(**kwargs):
     temp_dict = kwargs
     print(temp_dict)
     res = {}
     for i in range(len(temp_dict)):
         for item, value in temp_dict.items():
             print(value)
             if hash(value):
                 value
             else:
                 value = ','.join(value)

             res[value] = item
     print(res)
print(fun_key(arg1="Hello", arg2=2, arg3="123", arg4=[1, 2, 3, 4, 5]))