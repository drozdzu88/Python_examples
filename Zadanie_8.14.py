#Funkcja make car zapisująca informacje do słownika 
def make_car(mark, model, **kwargs):
	"""Budowa słownika zawierającego wszelkie informację na temat samochodu"""
	car_dic = {
	'mark_name': mark,
	'model_name': model,
	}
	for key, value in kwargs.items():
		car_dic[key] = value
	return car_dic

car_info = make_car('audi', 'a4', type='hatchback', seats_no=5)
print(car_info)
my_ford = make_car('ford', 's-max', type= 'minivan', seats_no=5)
print(my_ford)