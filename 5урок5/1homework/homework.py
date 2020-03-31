# создать модуль. В нем создать функцию, создающая директории от dir_1 до dir_2 
# затем создать вторую функцию которая удаляет эти папки
import os

 # name - иmя операционной системы
# chdir - смена текущей директории
# getcwd() - текущая рабочая директория
# mkdir() - создание директории (папки)
# os.path - модуль для работы с путями
# os.rmdir - удаляет пустаю директорию

# задание 1

# os.path.join(os.getcwd()  прокладывает путь к текущей дирректории и там создаёт папки

def my_dir():
	for i in range (1, 10):
		new_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i))
		# можно было сделать просто: folder_name = f'dif_{i}'
		os.mkdir(new_dir) # а внутри имя фолдер

	ans = input("папки созданы, проверь и нажми ентер" )

if __name__ == '__main__':
	my_dir()

def del_dir():
	for i in range (1, 10):
		os.rmdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))

	print('Теперь папки должны быть удалены')


if __name__ == '__main__':
	del_dir()
# задание 2

# создать модуль, в нём создать функцию которая будет принимать список и возвращать
# из него случайный элемнт. Если список Пуст, функция должна вернуть None 
import random

def check_list():
	my_list = []

	for i in range(1, 5):
		us_ans = input("Введите {} числo : ".format(i))
		my_list.append(us_ans)

	if my_list:
		var = random.choice(my_list)
		print(var)

# my_list = []

# for i in range(1, 5):
# 	us_ans = input("Введите {} числo : ".format(i))
# 	my_list.append(us_ans)
 
# print(check_list([])) # в таком случае, вернул бы None



