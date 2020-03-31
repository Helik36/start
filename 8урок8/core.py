# консульный файловый менеджер
# создание, удаление, копирование файлов и папок
# сохранение информации о своей работе в файл
import os
import shutil
import datetime
import random
# шаг 1  - создание файла


def create_file(name, text=None):
	with open(name, 'w', encoding='utf-8') as f:
		if text:
			f.write(text)

# шаг 2 - создание папки
def create_folder(name):
	try:
		os.mkdir(name)
	except FileExistsError:
		print('Такая папка уже есть')
# шаг 3 - показывать содержимое папки
def get_list(folders_only = False): # показыввет, что есть в текущей папке, а элемент  означается, что тольк папки
	result = os.listdir()
	if folders_only:
		result = [f for f in result if os.path.isdir(f)]
	print(result)

def delete_file(name):
	if os.path.isdir(name): # задаём условие - если наименование = файлу или дирректории
		os.rmdir(name) # удаляем директорию, но если папки нет
	else:
		os.remove(name) # удаляем файл

def copy_file(name, new_name): # копирование папок и файло
	if os.path.isdir(name):
		try:
			shutil.copytree(name, new_name)
		except FileExistsError:
			print('Такая папка уже есть')
	else:
		shutil.copy(name, new_name)

def save_info(massage): # функ для тоздание папки, где сохраняется вреся
	current_time = datetime.datetime.now()
	result = f'{current_time} - {massage}'
	# print(result)
	with open('log.txt', 'a', encoding='utf-8') as f: # а - до запись. Будет постоянно добавлять что-то
		f.write(result + '\n')

def game():
	rand = random.randint(1, 100)
	print("загаданно число от 1 до 100. Угадай какое")
	ans = None
	while ans != rand:
		ans = int(input())
		if ans == rand:
			print("Ты угадал!")
		elif ans > rand:
			print("Нужно меньше")
		elif ans < rand:
			print("нужно больше")

def change_dir(name):
	os.chdir(name)
	print(os.getcwd())

if __name__ =='__main__':
	create_file('text.dat')
	create_file('text.dat', 'some text')
	create_folder('new_f1')
	get_list()
	get_list(True) # передаем тут инфу о том, чтобы жлемент был Тру
	delete_file('new_f1')
	delete_file('text.dat')
	copy_file('new_f', 'new2')
	create_file('text.dat')
	copy_file('text.dat', 'text2.dat')
	save_info('abc')
	game()