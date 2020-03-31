# работа с файлом в режиме байтов
# open('filename', wb')  - режим записи байтов
# open('filename', rb') - режим чтения
# параметр encoding  определяет кодировку
# open('filename', 'w', encoding = 'utf-8')

with open('bytes.txt', 'wb') as f: # отрываем файл на запись
	pass

with open('bytes.txt', 'rb') as f: # на чтение
	pass

# открываем файл в текстовом режиме с указанием кодировки
with open('bytes.txt', 'r', encoding='utf-8') as f:
	pass

 # запись байтов в файл
 # f.write(b'some bytes') - файл открыт в режиме wb
 # f.write('some str') - файл открыт в режиме w
 # в любом случае информация хранится в виде 0 и единиц
