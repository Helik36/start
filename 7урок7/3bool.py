# приведение типов к bool в питон

# истина: 'abc', [1], (1,), {1:'a'}, 10, 1.1,...
# Ложь: '', (), {}, None...

# строка
s = 'str'

# классичекий способ
if len(s) != 0:
	print('строка не пустая')
else:
	print("пустая")

# удобный способ
if s:
	print("Не пустая")
else:
	print("пустая")

# аналигично со списком и слоаварями и другими типами
l = [1, 2, 3]
d = {1: 'a'}

if len(l) !=0 and len(d) != 0:
	print("не пустые")
else:
	print("Пустые")

# удобный способ
if l and d:
	print("не пустые")
else:
	print("Пустые")