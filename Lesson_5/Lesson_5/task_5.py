# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


import random

with open('test_task_5.txt', 'w') as my_f:
    for _ in range(30):
        my_f.write(f'{random.randint(0, 10)} ')
with open('test_task_5.txt') as my_f:
    n_str = my_f.read().split()
    total = 0
    for el in n_str:
        total += int(el)

print(total)
