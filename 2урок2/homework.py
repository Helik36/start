# Задание 1
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

# my_list_1 = set(my_list_1)
# my_list_2 = set(my_list_2)

# my_list_1 = my_list_1 - my_list_2 # не самый лучшиий варик т.к если в первом списке будет 1 единиц, но их не будет во втором, они тоже удяляться
# print(list(my_list_1))

a = [1, 1, 1, 2, 2, 2, 2, 3, 4]
b = [2, 4, 5]

for number in a[:]:
	if number in b:
		a.remove(number)
print(a)

# Задание 2

date_us = int(input("Какой день? "))
mounth_us = int(input("Какой месяц "))
year_us = int(input("Какой год? "))
print(date_us, mounth_us, year_us, sep='.')

days = {
	'1': 'Первое',
	'2': 'Второе',
	'3': 'Третье',
	'4': 'Четвертое',
	'5': 'Пятое',
	'6': 'Шестое',
	'7': 'Седьмое',
	'8': 'Восьмое',
	'9': 'Девятое',
	'10': 'Десятое',
	'11': 'Одиннадцатое',
	'12': 'Двенадцатое',
	'13': 'Тренадцатое',
	'14': 'Четырнадцатое',
	'15': 'Пятнадцатое',
	'16': 'Шестннадцатое',
	'17': 'Семнадцатое',
	'18': 'Восемьнадцатое',
	'19': 'Девятьнадцатое',
	'20': 'Двадцатое',
	'21': 'Двадцать первое',
	'22': 'Двадцать второе',
	'23': 'Двадцать третье',
	'24': 'Двадцать четвертое',
	'25': 'Двадцать пятое',
	'26': 'Двадцать шестое',
	'27': 'Двадцать седьмое',
	'28': 'Двадцать восьмое',
	'29': 'Двадцать десятое',
	'30': 'Тридцатое',
	'31': 'Тридцать первое',
}

mounth = {
	'1': 'Января',
	'2': 'Февраля',
	'3': 'Марта',
	'4': 'Апреля',
	'5': 'Майя',
	'6': 'Июня',
	'7': 'Июля',
	'8': 'Августа',
	'9': 'Сентября',
	'10': 'Октября',
	'11': 'Ноября',
	'12': 'Декабря'
}

result = "{} {} {} года".format(days[str(date_us)],mounth[str(mounth_us)], year_us)
print(result)


# задание 3

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

result = []
for number in my_list_1:
	if my_list_1.count(number) == 1: #метод проверяет, сколько раз число входит в список. если число входит 1 раз, то добавляет
		result.append(number)
print(result)
