# -*- coding: utf-8 -*-
#  Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


nums = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}

with open('test_task_4.txt') as my_f, open('new_test_task_4.txt', 'w') as my_new_f:
    my_f_lines = my_f.readlines()
    for line in my_f_lines:
        data = line.split()
        russo = nums.get(data[0])
        my_new_f.write(f'{line.replace(data[0], russo)}')
