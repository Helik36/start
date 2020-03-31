# dump - сохранение объекта в формате json в файл
# dumps - преобразование объекта в json (в текст)
# load - загрузка объект из файлы
# loads - загрузка объекта из формата json (строки)

import json

friends = [
	{'name': 'Max', 'age': 23, 'phone': [123, 345]},
	{'name': 'Leo', 'age': 23}
]

# посмотрим тип объекта
print(type(friends))

# преобразуем список друзей в json
json_friends = json.dumps(friends)

# печатаем, что получилось
print(json_friends)
# проверяем тип
print(type(json_friends))

# обратно из json в объект
friends = json.loads(json_friends)

print(friends)
print(type(friends))