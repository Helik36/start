ale = 71
age = int(input('Сколько вам лет? '))

print('Ваш возврат равне среднй продолжительности жизни', ale == age)
print('ваш возвраст НЕ равен среднй продолжительности жизни', ale != age)
print('Ваш возврат меньше среднй продолжительности жизни', age < ale)
print('ваш возвраст больше средней продолжительности жизни', age > ale)
print('Ваш возвраст меньше или равен средней продолжительности жизни', age <= ale)
print('ваш возвраст больше или равен средней продолжительности', age >= ale)

print('у вас юбилей: ', age % 5 == 0)