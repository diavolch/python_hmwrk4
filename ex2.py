# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def return_dict(**kwargs):
    my_dict = {}
    for key, name in kwargs.items():
        my_dict[str(name)] = key
    return(my_dict)

print(return_dict(arg1=5, arg2='word', arg3=[1,2,3], arg4=4))