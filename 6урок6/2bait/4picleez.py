# dump - сохранние объекта  в файл
# dumps - преобразование объекта в байт
# load - загрузка объекта из файла
# loads - загрузка объекта из набора байт

import pickle

person = {'name': 'Max', 'phones': [123, 345], 'age': 20} # можно постоянно менять

# открываем файл
with open('person.dat', 'wb') as f:
	pickle.dump(person, f)

print("Объект записан")

# открываем файл 
with open('person.dat', 'rb') as f:
	person = pickle.load(f)

print(person)
