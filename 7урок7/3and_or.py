import math

numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# создать список из тех чисел которые не имеют квадрный корень 2 [1, 2, 3]

result = []
# обычный способ
for number in numbers:
	if number > 0:
		sqrt = math.sqrt(number)
		# квадрный корень меньше 2
		if sqrt < 2:
			result.append(number)
print(result)

result = []
# через ленивый and
for number in numbers:
	if number > 0 and math.sqrt(number) < 2: # т.к первое будет выполнять, то и второе тоже
		result.append(number)
print(result)

# через генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)