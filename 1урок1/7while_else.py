#name = None

#while True:
#	name = input("Кто создатель python ")
#	if name == "Гвидо":
#		break # выходит из условие, если угадал
#	print("НЕ верно")

#print("Верно")

#number = 0
#n = int(input("Введите число: " ))

#while number <= n:
#	if number % 2 == 0: 
#		number += 1
#		continue # если число будет четное, условие продолжается, а если нечетное, то печается и к ней прибавляем число
#	print(number)
#	number += 1


number = 0
while number <= 100:
	print(number)
	number += 1
	if number == 33:
		break
else:
	print("else - end") # данное условие, выполниться только тогда, когда выполниться цикла

print("end") #  он выполниться  любом случае, когда выйдет из цикла