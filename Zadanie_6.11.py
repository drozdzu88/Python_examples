cities = {
	'warszawa': {
		'country' : 'polska',
		'area': 517.2,
		'population': 1.791,
	},
	'londyn':{
		'country' : 'anglia',
		'area': 1572,
		'population': 8.962,
	},
	'paryż':{
		'country' : 'francja',
		'area': 105.4,
		'population': 2.148,
	},
}

for country, facts in cities.items():
	print(f"\nMiasto {country.title()}:")
	print(f"\tZnajduje się w {facts['country'].title()}.")
	print(f"\tJego powierzchnia to {facts['area']} km2.")
	print(f"\tMieszka w nim {facts['population']} miliona osób.")