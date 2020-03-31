friend = {
	'name': 'Max',
	'age': 23,
	'has_car': True
}

# по ключам
for key in friend.keys(): # получаем только сами ключи (названия)
	print(key) # выводим название
	print(friend[key]) # выводим значение ключа

	# for key in friend # это всё тоже самое, что и сверху без функции key
	# print(key)
	# print(friend[key]) 

# по значению
for val in friend.values():
	print(val) # даёт просто значения

# пары ключ значение
for item in friend.items():
	print(item)

for key, val in friend.items():
	print(key)
	print(val)