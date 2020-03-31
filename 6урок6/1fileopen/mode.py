# r - чтение
# w - запись, если файла нет, создаётся новй
# x - запись, если файлна нет - ошибка
# а  - до запись
# b  - двоиный режим
# +  - открытие на чтение и запись 

f = open('first.txt', 'w')


# f = open ('second.txt', 'r')  - выдаст ошибку т.к файла  не существует

f = open ('first.txt', 'r') # производиться просто чтение

# write - запись ттроку в файл
# writelines - записать список строк в файл

f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'World\n'])

# read - чтение всего файла
# for line if f: - чтение файла построчно
# readlines - чтение файла в список строк

# print(f.read())

for line in f:
	print(line.replace('\n', ''))

print(f.readlines())

# f.close() - Закрытие. Но если то close будет искючительная ситуация, он не закроет
# with  - удобнее использовать


f.close() # нужно постояно помнить о вызовые

with open('first.txt', 'r') as f:
	for line in f:
		print(line.replace('\n', ''))

print('end')