# f.read() - файл открыт в режиме rb - читаем байты
# f.read() - файл открыт в режим r  - читаем строки

# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
	str = "Привет мир"
	f.write(str.encode('utf-8')) # кодираем 

# тоже самое, что сверхку
with open('bytes.txt', 'w',encoding='utf-8') as f:
	# пишем строку в байт
	f.write('привет мир')


# Открываем файл в режими чтения байтов
with open('bytes.txt', 'rb') as f:
	# читаем байты
	result = f.read() # читаем
	print(result) # выводим результ
	print(type(result))
	# декодируем для получение строки
	s = result.decode('utf-8')  # декодируем
	print(s)