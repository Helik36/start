import random

number = random.randint(1, 100)

user_number = None

count = 0
levels = {1: 10, 2: 5, 3: 3} 
level = int(input("Выберите уровень сложности от 1 до 3: "))
max_count = levels[level] 


user_count = int(input("Введите количество игроков: ")) # создаём количество игроков
users = []  # создаём пустой массив
for i in range(user_count): # делаем счётчик до номера пользователей
	user_name = input(f"Введите имя: {i}: ")
	users.append(user_name)
print(users)

is_winner = False #  Переменная с  ложью
winner_name = None # Пустая переменная

while not is_winner: # пока не ложь

	count += 1
	if count > max_count:
		print("Все пользователи проиграли")
		break

	print(f'Попытка № {count}')

	for user in users:
		print(f"Ход пользователя {user}" )
	
		user_number = int(input("Введите число: "))
		if user_number == number:
			is_winner = True
			winner_name = user
			break

		elif number < user_number:
			print("Ваше больше загаданного")
		else:
			print("ваше число меньше загаданного")
else:
	print(f"Победитель: {winner_name}")
