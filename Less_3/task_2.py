# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def my_func(name, surname, year, city, email, telephone):
    return f'{name}, {surname}, {year}, {city}, {email}, {telephone}'

name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
phone = input('input telephone')

per_data = my_func(name = name , surname = surname, year = year, city = city,
              email = email , telephone = phone)
print(per_data)
