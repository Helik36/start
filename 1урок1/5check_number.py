number = 45
value = int(input("введите числа: "))

if value == number:
	print("Вы угадали!")
else:
	if value > number:
		print("Нужно меньше")
	else:
		print("Нужно больше")