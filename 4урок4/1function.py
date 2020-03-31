#abs - модуль числ
# min, max -  минимальное и макс значение
#round - округление числа
# sum - сумма элементов полсдеовательности
# enumerate нумерация последовательсти

print(abs(-7))
numbers = [5, 15, 7, -9, 0]
print(max(numbers))
print(min(numbers))

print(round(10.9872, 2)) # знак 2 означается, что будет выводит 2 знака после запятой

print(sum(numbers))

winners = ['Leo', 'Max', 'kate']
for numbers, winner in enumerate(winners, 1): # 1 значит, что нумерация будет с 1
	print(numbers, winner)