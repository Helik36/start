# Задание 1
number = int(input("Введите число: "))

sum = number + 2
print("твоё число с + 2 ровно: ", sum)

# задание 2

number = int(input("Введите число от 0 до 10: "))
while True:
	if number < 0 or number > 10:
		number = int(input("Нет, ввидете число от 0 до 10: "))
		continue
	else:
		step = number ** 2
		print("Твоё число в степени ровно: ", step)
		break

# задание 3

print("Это Мед анкета. Заполните о себе данные")

name = input("Ваше имя: ")
two_name = input("Ваша Фамилия: ")
age = int(input("Ваш возвраст: "))
mass = int(input("Ваш весс: "))

if age < 30 and mass > 50 and mass < 120:
	print("Пациент в норме")

elif age >= 30 and age <= 40 and mass < 50 or mass > 120:
	print("Вам нужно заняться собой")

elif age > 40 and mass < 50 or mass > 120:
	print("Вам нужно к врачу")

else:
	print("Вы в порядке")