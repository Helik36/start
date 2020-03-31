import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, game, change_dir

save_info('Старт')
try:
	command = sys.argv[1]
except IndexError:
	print('нужно выбрать команду. Если ты их не знаешь, напищи - help')
else:
	if command == 'list':
		get_list()

	elif command == 'create_file':
		try:
			name = sys.argv[2]
		except IndexError:
			print("Отсутсвует название файла")
		else:
			create_file(name)

	elif command == 'create_folder':
		try:
			name = sys.argv[2]
		except IndexError:
			print("Отсутсвует название файла")
		else:
			create_folder(name)

	elif command == 'delete':
		try:
			name = sys.argv[2]
		except IndexError:
			print("Вы не указали назваание удаляемого файла или проекта")
		else:
			delete_file(name)

	elif command == 'copy':
		try:
			name = sys.argv[2]
			new_name = sys.argv[3]
		except IndexError:
			print("Вы не указали название папки которую нужно скорпировать или не задано")
		else:
			copy_file(name, new_name)

	elif command == 'game':
		game()

	elif command == 'ch':
		try:
			name = sys.argv[2]
		except IndexError:
			print("Вы не указали название папки которую нужно скорпировать или не задано")
		else:
			change_dir(name)

	elif command == 'help':
		print('list - список файлов и папок')
		print('create_file - создание файла')
		print('create_folder - создание файлов')
		print('delete - удаление файла или папки')
		print('copy - копирование файла или папки')
		print('ch')
		print('game - поиграть в игру - угадай число')

save_info('Конец\n')