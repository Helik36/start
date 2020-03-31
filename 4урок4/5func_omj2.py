def my_filter(numbers, function):
	result = []
	for number in numbers:
		if function(number):
			result.append(number)
	return result

def is_even(number):
	return number % 2 == 0

numbers = [1,2,3,4,5,6,7,8]
print(my_filter(numbers, is_even))


#Если нужны не чтные числа

def is_not_even(number):
	return number % 2 != 0

print(my_filter(numbers, is_not_even))

# если нужны числа, больше 4

def big_4(number):
	return number > 4

print(my_filter(numbers, big_4))