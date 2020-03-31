# создать список из случайных чисел от 1 до 100

import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# создаем список квадратов чисел
numbers = [1, 2, 3, -4]

numbers = [numbers**2 for numbers in numbers]
print(numbers)

# создать список имен на букву А
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']

names = [name for name in names if name.startswith('А')]
print(names)