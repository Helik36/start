#sys.argb - список аргументов командной строки при запуски скрипта питон

# sys.argb[0] - путь до скрипта
# остальные параметры передаются при вызов скрипта через проблем
# python my_script.py par1 par2 par 3

import sys

# print(sys.argv[0])
for arg in sys.argv: # можно указывать там какие то параметры
	print(arg)
	print(type(arg))