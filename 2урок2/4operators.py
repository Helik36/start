hero = 'Superman'

if hero.find('man') != -1:
	print("Есть")

# как делает с in
if 'man' in hero:
	print("Есть")

goals = ['стать гуру языка python', 'здоровье', 'накормить кота']

if 'здоровье' in goals:
	print('все хорошо')

#кортеж (tuple) - список, который нельзя изменить. Записаться в круглые скобки. Служить для защиты от изменений
print("СОРЕВНОВАНИЕ ПО PYTHON")
count = int(input('Введи количество участников: '))
i = count
members = []
while i > 0:
	name = input('Кто занят {} место: '. format(i))
	members.append(name)
	i -= 1

print('В соревнованиях участвовали: ', sorted(members)) # sorted сортирует по альфавиту

# мы записали людей с конца?
members.reverse() # Так 5 место вы объявили первым, оно будет последним, дабы соответсвовало самому месту выйгрыша

# нам нужно взять первые 3 места
result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)