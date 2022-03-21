# DZ_2
# Задание 1

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Задание 2

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

corr_list = []
for i in my_list:
	if i.isdigit():
		corr_list.extend(['"', f'{int(i):02}', '"'])
	elif i.startswith('+') or i.startswith('-') and i[1:].isdigit():
			new_list.extend(['"', f'{i[0]}{int(i[1:]):02}', '"'])
	else:
		corr_list.append(i)
out_list = ' '.join(corr_list)
print(out_list)

# Задание 3

list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in list_1:
	name = i.split(' ')
	name = (name[-1].lower())
	name = name[0].upper() + name[1::]
	print('Привет: ', name)

#  Задание 4

prices = sorted([23, 14.24, 41, 2.15, 54.2, 97.35, 12.4, 88, 52.41,
          42, 144.41, 56, 745, 67.56, 1052.34, 315, 921.1])
print(id(prices))
for price in prices:
	rub = int(price)
	kk = (price - rub) * 100
	print(f'{rub} руб {kk:02.0f} коп', end=', ')
print()
print(id(prices))

prices = (sorted([23, 14.24, 41, 2.15, 54.2, 97.35, 12.4, 88, 52.41,
          42, 144.41, 56, 745, 67.56, 1052.34, 315, 921.1][::-1][:5]))
for price in prices:
	rub = int(price)
	kk = (price - rub) * 100
	print(f'{rub} руб {kk:02.0f} коп', end=', ')