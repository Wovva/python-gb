# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


with open('test_task_2.txt') as my_f:
    my_f_lines = my_f.readlines()

str_count = 0
for num, line in enumerate(my_f_lines):
    str_count += 1
    words_count = len(line.split())
    print(f'#{num + 1} - {words_count} words.')
print(f'{str_count} strings.')
