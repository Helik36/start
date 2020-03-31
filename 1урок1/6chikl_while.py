#name = input("кто создатель python? ")

#while name != "Гвидо":
#	print("Не верно")
#	name = input("Кто создатель python ")

#print("Верно")

number = 0
n = int(input("Введите число: " ))

while number <= n:
	if number % 2 == 0: # если нужны не четные, то numbber % 2 !=0:
		print(number)
	number += 1