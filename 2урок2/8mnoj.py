# Семейная пара собирается в отпуск
# каждый из супругов собирает вещи
# Max взял эти вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}

#Kate взяла эти вещи:
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# Какие вещи взяли супруги
print(max_things | kate_things) # объединение
# какие вези повторяются
print(max_things & kate_things) # пересеченине
#Какие вези взял мах, но не взяла кате
print(max_things - kate_things) # вычетамем вещи которые взяли оба и выводим те, которые взял мах
# какие вещи взяла кате но не взял мах
print(kate_things - max_things)