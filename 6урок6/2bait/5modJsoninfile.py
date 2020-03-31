import json

friends = [
	{'name': 'Max', 'age': 23, 'phone': [123, 345]},
	{'name': 'Leo', 'age': 23}
]

# посмотрим тип объекта
print(type(friends))

# открываем файл
with open('friends.jon', 'w') as f:
	# преобазуем список друзей в json и сохраняем в файл
	json_friends = json.dump(friends, f)

# образуем обратно из файла в объекта
with open('friends.jon', 'r') as f:
	friends = json.load(f)

print(friends)
print(type(friends))