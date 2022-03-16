# dz 1
# Задание 1
duration = int(input('Введите время в секундах: '))

day = duration // (3600 * 24)
hour = (duration - day * (3600 * 24)) // (60 * 60)
minute = (duration - day * (3600 * 24) - hour * (60 * 60)) // 60
second = (duration - day * (3600 * 24) - hour * (60 * 60) - minute * (60))

if duration < 60:
	print(duration, 'секунд')
elif duration >= 60 and duration < 3600:
	print(minute,'мин', second,'сек')
elif duration >= 3600 and duration < 86400:
	print(hour, 'час', minute, 'мин', second, 'сек')
elif duration >= 86400:
	print(day, 'день', hour, 'час', minute, 'мин', second, 'сек')

# Задание 2
my_list = [(list_1 ** 3) for list_1 in range(1, 1001, 2)]
result = 0
for num in my_list:
	ch_sum = 0
	for ch_num in str(num):
		ch_sum += int(ch_num)
	if ch_sum % 7 == 0:
		result += num
print(result)
# # b
my_list = [(list_1 ** 3) for list_1 in range(1, 1001, 2)]
result = 0
for num in my_list:
	num += 17
	ch_sum = 0
	for ch_num in str(num):
		ch_sum += int(ch_num)
	if ch_sum % 7 == 0:
		result += num
print(result)
# Задание 3
percent = int(input('Введите число: '))
if percent == 1 or (percent // 10 >= 2 and percent % 10 == 1):
    print(percent,'Процент')
elif 2 <= percent <= 4 or (percent // 10 >= 2 and 2 <= percent % 10 <= 4):
    print(percent,'Процента')
else:
    print(percent,'Процентов')


