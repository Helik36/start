# мы можем импортировать 
import math
# но не сможем импортировать наш модуль например на диске C:
# import mymodule

# Как питон находит модул

import sys

print(sys.path)
print(type(sys.path))

for p in sys.path:
	print(p)

sys.path.append('D:')
import mymodule # что то с доступом, по этому пока не показывает на С