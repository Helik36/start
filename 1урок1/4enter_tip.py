name = input('Как тебя зовут? ')
print(type(name))

age = int(input('Сколько тебе лет? ')) #Чтобы сложить число с числом, нужно привести к правильному типу
print(type(age))

is_love = input('вы любите питон? ')
print(type(is_love))

period = 20
age_period = period + age
print('Через ', period, ' вам будет ', age_period)