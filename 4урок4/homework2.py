#Вычеслять и возвращать полученный урон по формуле дамаг/армор
#должно быть 2 функции 1)наносит уроню
# 2)вычисляет урон по отношению к броне.
# функция 2 используется внутри номер 1 для вычесления урона и вычитания его из здоровья
# персонажаю
def tactic(person1, person2): 

	def armorr(): 
			return round(person1['damage']/person2['armor'], 2) # округляем до 2 знаков после запятой

	person2['health'] = person2['health'] - armorr()
	for i, j in enemy.items():
		print(i,':', j)

player = {
	'health': 100,
	'damage': 50,
	'armor': 1.2
}
player['name'] = input("Укажи имя героя: ")

enemy = {
	'name': 'PC',
	'health': 100,
	'damage': 50,
	'armor': 1.2
}

tactic(player, enemy)