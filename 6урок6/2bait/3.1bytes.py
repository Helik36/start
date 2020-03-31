 # запись байтов в файл
 # f.write(b'some bytes') - файл открыт в режиме wb
 # f.write('some str') - файл открыт в режиме w
 # в любом случае информация хранится в виде 0 и единиц


# Открываем файл дляя записи байтов
with open('bytes.txt', 'wb') as f:
	# пишем строку в байт
	f.write(b'Hello bytes') 

# Читаем как текст
with open('bytes.txt', 'r', encoding='ascii') as f:
	# пишем строку байт
	print(f.read())

открываем файл для записи байтом
with open('bytes.txt', 'wb') as f:
	# пишем строку байт
	str = 'привет мир'
	f.write(str.encode('utf-8'))

# Читаем как текст с кодировкой ютф-8
with open('bytes.txt', 'r', encoding='utf-8') as f:
	# пишем строку в байт
	print(f.read())

# f.read() - файл открыт в режиме 