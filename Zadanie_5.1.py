age = 32
print('Czy age == 32? Przewiduję wartość True')
print(age == 32)

print('\nCzy age ==40? Przewiduję wartośc False')
print(age == 40)

cars = ['bmw', 'audi', 'reno', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


favorite_car = 'skoda'
if favorite_car in cars:
	print(f"{favorite_car.title()} jest jednym z Twoich ulubionych samochodów")
else:
	print(f'{favorite_car.title()} nie jest na liście Twoich ulubionych aut')


if 'ford' in cars:
	print(True)
else:
	print(False)


if favorite_car not in cars:
	print(f"Całe szczęśćie, że nie kupiłeś {favorite_car.title()}")
else:
	print(f"{favorite_car.title()}, to dobry wybór")


#blok z deklaracją ulubionych liczb i ich posortowanie 
favorite_numbers = [5, 6, 8, 7, 10, 32, 13,]
favorite_numbers.sort()
print(favorite_numbers)

	#blok z if'ami
number_1 = 10
number_2 = 13

if number_1 in favorite_numbers and number_2 in favorite_numbers:
	print(True)
else:
	print(False)

if 2+2 not in favorite_numbers and 20-6 not in favorite_numbers:
	print(True)
else:
	print(False)
		
number_3 = 200
number_4 = 50

if 100+50 == number_3 or 100+50 >= number_4:
	print('Wszystko Ok')	


