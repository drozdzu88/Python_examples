def build_profile(first, last, **user_info):
	"""Budowa słownika zawierającego wszystkie informacje o użytkowniku."""
	profile={}
	profile['first_name'] = first.title()
	profile['last_name'] = last.title()
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location='pirnceston', field='fizyka')
print(user_profile)

user_profile = build_profile('łukasz', 'drozd', age='32', sex='male', height=188)
print(user_profile)