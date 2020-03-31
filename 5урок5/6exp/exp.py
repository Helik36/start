# в зависимости от параметра, вызывать различные функции скрипта
# параметр pint -> функция выводит pong
# 2 параметра name <Имя> -> функция приветстви пользователя
# Параметр list показать содержимое текущей директории

import sys, os

def ping():
	print('pong')

def hello(name):
	print('Hello,', name)

def get_info():
	print(os.listdir())

command = sys.argv[1] # в этом коде в СМД нужно помимо вызова самой проги задать
 # какие то условия

if command == 'ping': # если пишем пинг, то выводится понг
	ping()
elif command == 'list':
	get_info()
elif command == 'name': # тут уже нужно написать name и само имя
	name = sys.argv[2] # по этому тут уже будет 2 параметра
	hello(name)
