# args - передача любого кол-ва по порядку
#kwargs = передача любого кол-ва по имени


def greeting(say, *who): # args
	print(say, who)


greeting('Hello', 'Leo')

greeting('Hello', 'Leo', 'Max') # т.к мы поставили звёздочку, будет передачаться значение неограниченно

def get_person(**kwargs):
	for k, v in kwargs.items():
		print(k, v)

get_person(name = 'Leo', age =20, has_car = True) # Можно передать любое количество по имени