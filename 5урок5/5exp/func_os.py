# name - иmя операционной системы
# chdir - смена текущей директории
# getcwd() - текущая рабочая директория
# mkdir() - создание директории (папки)
# os.path - модуль для работы с путями
# и многие дргие

import os
#имя операционной системы
print(os.name)

# Текущая рабочая директория
print(os.getcwd())

#создаем новые пути
new_path = os.path.join(os.getcwd(), 'new_f')

# создаем папку по новому поути
os.mkdir(new_path)