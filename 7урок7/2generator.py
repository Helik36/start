# cинтаксис
# [number for number in numbers if number > 0]

# записать в список только полож. числа
numbers = [1,2,3,4,5, -1,-2,-3]

# классика
result = []
for number in numbers:
	if number > 0
	result.append(number)

# через фильтер

result = filter(lambda number: number > 0, numbers)
print(list(result))

# через генератор
		  # переменная		цикл		условие
result = [number for number in numbers if number > 0]
print(result)

