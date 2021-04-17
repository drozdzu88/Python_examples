first_list = list(range(1,10))
print(first_list)

for number in first_list:
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f'{number}nd')
	elif number >= 3:
		print(f'{number}th')
