global_var 1

def my_f():
	#global my_var - указав значение глобал, мы можем внетри этой функции менять значение
	#но это вдруг её вызову гдето в другом место, то значение будет уже другой, а не изначальное
	local_var = 100
	print(local_var)
	print(global_var)
	#global_var = 999 # выдаст ошибку т.к глобальную перменную нельзя поменять


my_f()
print(global_var)
#print(local_var) # выдаст ошибку, т.к она локально есть только в функции

#_______________________________________ пример, почему лучше не менять
global_var = 2

def my_f():
	result - global_var ** 5

def my_chance_f():
	global global_var
	global_var = "Какая то строка"

my_chance_f()
my_f()