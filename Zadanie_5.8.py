user_list = ['luke', 'admin', 'kasia113', 'pawel987', 'karolina']

if user_list:
	for user in user_list:
		if user == 'admin':
			print(f"Wiatj, {user}! Czy chcesz przejrzeć dzisiejszy raport?")
		else:
			print(f"Witaj, {user}! Dziękujemy, że ponownie się zalogowałeś")
else: 
	print('Musimy znaleść jakichś użytkowników')