# задание 1

a = ['Яблоко', 'Мандарин', 'Личи', 'Ананас']
b = ['Апельсин', 'Банан', 'Яблоко', 'Личи', 'Груша']

c = [name for name in a if name in b]
print(c)


# задание 2

numbers = [-10, -9, -8,- 7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number2 = [num for num in numbers if num > 0 and num % 3 == 0 and num % 4 != 0]
print(number2)

# задание 3
import math

def my_func(numbers):
	a =  [math.sqrt(num) if num > 0 else num for num in numbers]
	return print(a)

numbers = [-100, -81, -80,- 70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 81, 100]

my_func(numbers)
print(numbers)

# задание 4

def new_func(a):
	if a == 13:
		raise ValueError(" о о о о шбика")
	else:
		a = a**2
	return print(a)


# try:
	a = new_func(int(input("введи число от 1 до 100: ")))
# except ValueError:
# 		print("цифра 13")