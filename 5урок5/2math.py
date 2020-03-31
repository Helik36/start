# math
# factorial - факториал числа
# exp - экспонент
# log, log2, log10 - логарифмы
# sqrt - квадратный корень
# sin cos, asin, acos ...
# и другие

import math
#найти длину окружности
r = 100
print(2*r*math.pi)

#найти площадь окружности
print((r**2)*math.pi)
print((math.pow(r, 2))*math.pi)

# по координатам 2-х точек определить расстояние между ними
x1=10
y1=10
x2=50
y2=100

1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(1)

#найти факториал числа 9 

print(math.factorial(9))