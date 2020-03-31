# читаем объект из файла

# открываем файл

with open('person.dat', 'rb') as f:
	# теперь нам надо знать как мы записывали объект
	# прочиатем файл в список
	result = f.readlines()

# теперь воссоздаём исходный объект
person = {}
# первый элемент - это имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телефоны
phones = []
for bhphone in result[1:]:
	phones.append(bhphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

print(person)
# получили исходный объект. Это было тяжело. А что, если он немного измениться?