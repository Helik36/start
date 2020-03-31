# Пикли
# dump - сохранние объекта  в файл
# dumps - преобразование объекта в байт
# load - загрузка объекта из файла
# loads - загрузка объекта из набора байт

# джсон
# dump - сохранение объекта в формате json в файл
# dumps - преобразование объекта в json (в текст)
# load - загрузка объект из файлы
# loads - загрузка объекта из формата json (строки)


import pickle, json

my_favourite_group = {
	'name': 'Г.М.О', 
	'tracks': ['Последний месяц осени'], 
	'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]}

print(my_favourite_group)

p_group = pickle.dumps(my_favourite_group)
print(p_group)
with open('group.pickle', 'wb') as f:
	pickle.dump(my_favourite_group ,f)


print('group.pickle создан')

j_group = json.dumps(my_favourite_group)
print(j_group)
with open('group.json', 'w', encoding='utf-8') as f:
	json.dump(my_favourite_group, f)


print('group.json создан')

