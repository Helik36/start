cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']

print(type(cities))
print(cities)

cities = set(cities)
print(cities)
print(type(cities))

cities = {'Las Vegas', 'Paris', 'Moscow'} # можно писать так сразу

cities.add('Burna')
print(cities)
cities.add('Moscow')
print(cities)

cities.remove('Moscow')
print(cities)

print(len(cities))

print('Paris' in cities)

for city in cities:
	print(city)