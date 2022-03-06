#Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("test_task_1.txt", "w") as out_f:
    line = ()

    while line != "":
        line = input('Enter str or " ":')
        out_f.writelines(f'{line}\n')
        if line == "":
            break
print(type(line))
