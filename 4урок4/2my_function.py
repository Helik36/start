
def print_sep(sep, sep_len): # указываем название переданного параметра
	# print(sep * sep_len) # вызываем его тут
	return sep * sep_len # .. нужно чтобы тут, функция возвраща итог значения

print("Моя первая функция")
print(print_sep('-', 100))  # передаём параметр
print("Красивый разделитель")
print(print_sep('*', 100))

print(print_sep('-', 100)) # передаём параметр
print(print_sep('*', 100))

print(print_sep('*', 50))

sep = print_sep('-', 50) # Чтобы тут sep приял значние фунукции...
text = 'Hello {} Func {}'.format(sep, sep)