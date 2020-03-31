# комп загадывает от 1 до 100, мы угадываем

# Шаг 1, нужн загадать случайное число
import random

number = random.randint(1, 100)

user_number = None

count = 0
levels = {1: 10, 2: 5, 3: 3} # создали библиотеку уровней. ключ, а в нём попытки
level = int(input("Выберите уровень сложности от 1 до 3: "))
max_count = levels[level] # смотрит по ключу

while number != user_number: 

	count += 1
	if count > max_count:
		print("Вы проиграли")
		break
	print(f'Попытка № {count}')
	
	user_number = int(input("Введите число: "))

	if number < user_number:
		print("Ваше больше загаданного")
	elif number > user_number: 
		print("ваше число меньше загаданного")
	else:
		print("Победа")
