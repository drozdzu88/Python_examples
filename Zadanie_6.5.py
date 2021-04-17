Important_rivers = {
	'nil': 'egipt',
	'wisła': 'polska',
	'ren': 'francja'
}

for key, value in Important_rivers.items():
	print(f"{key.title()}, płynie przez {value.title()}.")

print("\n")

for key in Important_rivers.keys():
	print(key.title())
print("\n")

for value in Important_rivers.values():
	print(value.title())