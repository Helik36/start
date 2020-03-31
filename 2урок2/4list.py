empty_list = []

friends = ['Max', 'Leo', 'Kate']
print(type(friends))

print("Второй друг: ", friends[1])
print("Первый друг с конца: ", friends[-1])

#примерение срезы
print(friends[1:2])
print(friends[:2])
print(friends[0:])

#len(friends) - Длина списка (сколько в нём элемнтов)
#friends.append() - добавление нового элемента
#friends.pop() - удаляем последний элемент и возвращаем его
#friends.clear() - очищаем весь список
#friends.remove() - удаление объекта из списка
#del friends[0] - удаление элемента по списку

print(len(friends))

friends.append('Ron') # добавили в список

print(len(friends))

print(friends.pop()) # Удаляем последний элемент списка

print(len(friends)) # выводим длину массива

friends.remove('Kate')  # Удаляем Кэйт

print(friends)

del friends[0] # удаляем по номеру элемента

print(friends)