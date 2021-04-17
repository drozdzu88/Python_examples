pizza_list = ['margarita', 'capriciosa', 'hawaii']
friend_pizza = pizza_list[:]

pizza_list.append('wiejska')
friend_pizza.append('pepperoni')

print("Moje ulubione pizze to:")
for my_pizza in pizza_list:
	print(my_pizza)

print("\nUlubione pizze mojego kolegi to:")
for his_pizza in friend_pizza:
	print(his_pizza)