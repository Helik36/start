def some_f():
	return 10


result = some_f()

print(result)

a = some_f

print(a)
print(type(a))

a() # будет тоже самое, что и some_f

#______________________________________________________
def f():
	print("Hello from other f")

def to(f_param):
	f_param()

to(f)