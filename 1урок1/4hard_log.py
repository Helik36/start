ale = 71
age = int(input('Сколько вам лет? '))

print('у вас юбилей: ', age % 5 == 0)

# not and or
print('У вас не юбилей: ', age % 5 != 0)
print('у вас не юбилей: ', not age % 5 == 0)

# and
print('у вас юбилей и ваш возвраст меньше средней продолительности жизни: ', age % 5 == 0 and age < ale)

# or 
print('У вас юбилей или ваш возвраст меньше средней: ', age % 5== 0 or age < ale)

# приоритет в лог выражениях
print(1 > 2 and (0 < 5 or 0 < 2) and 0 == 0)