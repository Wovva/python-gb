# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    sum_a = arg_1 + arg_2 + arg_3
    return sum_a - min(arg_1, arg_2, arg_3)
x = int(input('Введите значение: '))
y = int(input('Введите значение: '))
z = int(input('Введите значение: '))
sum_xyz = my_func(x, y, z)

print(sum_xyz)
