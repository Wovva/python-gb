# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if y >= 0:
        return 'Y должен быть отрицательный'
    return x ** y

x = float(input('Введите действительное положительное число X: '))
y = int(input('Введите целое отрицательное число Y: '))

print(my_func(x, y))