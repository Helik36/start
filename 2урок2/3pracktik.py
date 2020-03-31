top5 = "Первые 5 мест на соревнованиях: 1. иванов 2. петров. 3. сидоров 4. орлов 5. соколов"

start = top5.find('1')
end = top5.find('4')

top3 = top5(start: end)

result = "Поздравляем {} с усехом!".format(top3upper())

print(result)