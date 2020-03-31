m = "меня видно везде"

def a():
	ma = 'Меня видно в b() и  а()'

	def b():
		print(m)
		print(ma)
		mb = 'меня видно в с() и в b(), но не видно в а'

		def c():
			print(m)
			print(ma)
			print(mb)
			mc = "меня видно только в c"

		#print(mc) - выдаст ошибку т.к она идёт в b а она только в с

		c()

	b()
a()