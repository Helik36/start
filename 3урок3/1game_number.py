# комп загадывает от 1 до 100, мы угадываем

# Шаг 1, нужн загадать случайное число
import random

number = random.randint(1, 100)
# print(number)


while True: # 4 шаг, сделать цикл, который будет спрашивать, пока не угадаешь

	# Шаг 2 Предложить пользователю ввести число
	user_number = int(input("Введите число: "))
	print(user_number)

	# Шаг 3 Сравнить загаданное число с ответом пользовател
	if number == user_number:
		print("Победа")
		break
	elif  number < user_number:
		print("Ваше больше загаданного")
	else:
		# number > user_number: # т.к иного нет, это условие можно не ставить
		print("ваше число меньше загаданного")

