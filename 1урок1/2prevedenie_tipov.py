birthday_year = '1998'
print(type(birthday_year))

person = 20
print(type(person)) 

#age = birthday_year + person #Выдаст ошибку
#print(age)
#
#Нужно делать
age = int(birthday_year) + person
print(age)

age_int = birthday_year +str(person)
print(age_int)