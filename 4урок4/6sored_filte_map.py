# sorted  - сортировка последовательностей

numbers = [1,5,3,5,9,7,11]

print(sorted(numbers))

print(sorted(numbers, reverse=True))

names = ['Max' 'Alex' 'Kate']

print(sorted(names))

cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антвепен', 2000)]
#такая сортировка будет по алфавиту
print(sorted(cities))
#как отсортировать по численности населения

def by_count(city): ### тоже самое
	return city[1]

print(sorted(cities, key = by_count))
print(sorted(cities, key = lambda city: city[1])) ###

#__________________________________________________________
#filter - фильтрация последовательности

numbers = {1,5,3,5,9,7,11}

def is_even(number):
	return number % 2 ==0

result = filter(is_even,numbers)
print(result)
result = list(result)
print(result)


names = ['Max', 'Leo', ' Kate']

print(list(filter(lambda x: len(x)>3, names)))

#_____________________________________________________________________________
#map - применение функции к каждому элементу последовательности


numbers = [5,3,4,7,8]
#получение квадрата
print(list(map(lambda x: x ** 2, numbers)))
#привести числа к строке
print(list(map(lambda x: str(x), numbers)))