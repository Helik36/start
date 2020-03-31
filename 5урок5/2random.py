#randint - целое случачйно число от А до Б
# choice - случайный элемент последовательности
# shuffle - перемешать последовательность
# random - случайные числа от 0 до 1
# sample - список длинной k из последовательности 
# и другие
from random import randint, choice, sample
# 1 загадать случайное число от 0 до 100
print(randint(0, 100))
# выбрать победителя из списка 
players = ['leo', 'Max', ' Kate', 'Ron', 'Bill']
print(choice(players))
#выбрать 3-х победителей
print(sample(players, 3))
#перемещать последовательность в стопке
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
print(shuffle(cards))