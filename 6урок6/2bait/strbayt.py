# bytes - строки байт
# bytearray - изменяемая строка байт

# создание строки байт

sb = b'Hello bytes'

print(type(sb))
print(sb)

# индекс - sb[0]
# срез sb[1:3]
#...

print(sb[1]) # код буквы е

print(sb[1:3]) # 

for item in sb:
	print(item)