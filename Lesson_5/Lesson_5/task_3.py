# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.


with open('test_task_3.txt') as my_f:
    my_f_lines = my_f.readlines()

zpshka = {}
itogo = 0
for line in my_f_lines:
    zp_inf = line.split()
    zpshka.update({zp_inf[0]: float(zp_inf[1])})
    itogo += float(zp_inf[1])
sred_zp = itogo / len(zpshka)
print(f'Средняя ЗП = {sred_zp}')

for x, y in zpshka.items():
    if y < 20000:
        print(f'{x}: {y}')
