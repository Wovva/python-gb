#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
#Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_zp, first_param, second_param, third_param = argv



print("выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)

total = int(first_param) * int(second_param) + int(third_param)


print("Зарплата сотрудника: ", total)
