#строка целоиком
print('привет, меня зовут Кеша, мне 2 года')

#у нас есть 2 переменные
name = 'Кеша'
age = 2
#Как вывести строку вместе с переменными в терминал
print(name, age)

#Как вывести не через пробел, а черещ \
print(name, age, sep='/')
print(name, age, sep='/;h')

# end
print(name)
print(age)
#а можно
print('-------->')
print(name, end=';')
print(age, end=';')
print('and', end=';')

#Ввод данных
#result = input()
#print('пользователь ввел: ', result)
name = input('Как тебя зовут: ')
print('Привет,', name)
