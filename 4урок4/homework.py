# Задание 1

def you(name, age, city):
	return print(name, ',' , age, 'год, проживает в городе', city)
	
name = input("Твоё имя? ")
age = input("Возвраст? ")
city = input("Где живёшь? ")

you(name, age, city)

#Задание 2

def mmax(numbers):
	return max(numbers)

numbers = []
for i in range(3):
	user = int(input("Введи 3 разных числа: "))
	numbers.append(user)
print(mmax(numbers))
print(lambda numbers: max(numbers)) # выводит место в памяти,  не само число
		
# задание 3
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять количество от health
# атакущео.
#Функция должна работать со словарями и изменять их значение
def tactic(person1, person2): 
		person2['health'] = person2['health'] - person1['damage']
		print(person1['name'], 'наносит урона:', person1['damage'], 'игроку', enemy['name']) 
		if person2['health'] == 0:
			print("Враг умер") # но он не умрёт
		else:
			print("Враг жив, у него ещё: ", person2['health'], "хп")

player = {
	'health': 100,
	'damage': 50
}
player['name'] = input("Укажи имя героя: ")

enemy = {
	'name': 'PC',
	'health': 100,
	'damage': 50
}

tactic(player, enemy)