# range позволяет создать последовательность целых чисел
numbers = range(10)
print(numbers)
print(type(numbers))

print(list(numbers))

winners = ['Max', 'Leo', 'Kate']

for winner in winners:
	print(winner)

for i in range(len(winners)):
	#print(i)
	print(i + 1, ') ',winners[i])
# range имеет 3 параметра
# range(start_or_stop, stop[, step])
# start_or_stop - начало или конец последовательности
# stop - конец
# step - шаг

numbers = [1, 3, 5]

for number in numbers:
	print(number)
# но что, если нам нужно 1000 чисел
print(list(range(1, 1000, 2))) # стартуем с 1, конечный будет 1000, шаг 2

for number in range(1, 1000, 2):
	print(number)