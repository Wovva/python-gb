# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

firm = {}
pos_firm, pos_bal = 0, 0
with open('test_task_7.txt') as my_f:
    my_f_lines = my_f.readlines()

for line in my_f_lines:
    data = line.split()
    profit = float(data[2]) - float(data[3])
    firm.update({data[0]: profit})
    if profit > 0:
        pos_firm += 1
        pos_bal += profit

average_profit = pos_bal / pos_firm
result = [firm, {'average_profit': average_profit}]

with open('result.json', 'w', encoding='utf8') as my_f:
    json.dump(result, my_f)

with open('result.json', encoding='utf8') as my_f:
    result = json.load(my_f)
    print(result)