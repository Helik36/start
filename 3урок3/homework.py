# Человек заадывает число,а компьютер его отгадывает
import random


print("Привет. Меня зовут: Компик. Загадай число от 1 до 100")
print("Если я загадал число меньше, скажи, что нужно больше - '>', а если загадал больше, то нужно меньше - '<'.\nА если я угадал, то ответить: 'Да'\n")
number = 100 # указали, сколько всего цифр
numbers = []
numberr = 0

for i in range(number): # Сделал, чтобы в список добавилиссь элементы
	numbers.append(i)

for numberr in numbers: # прировнял элементы списка от 1 до 100
	numbers[numberr] = numberr + 1
print(numbers,'\n')

Max = max(numbers)
Min = min(numbers)

us_ans = None

while True:

	pc_ans = random.randint(Min, Max) # Доработать

	print(f"Ты загадал число {pc_ans}?")
	us_ans = input('\n')
	if us_ans == 'Правильно' or us_ans == 'правильно' or us_ans == 'да' or us_ans == 'Да':
		print("\nУра!")
		break

	elif us_ans == '>':
		Min = pc_ans

	elif us_ans == '<':
		Max = pc_ans

	else:
	 	print("Нужно ответить: < , > или - 'Да'\n")



