current_users = ['luke', 'admin', 'kasia113', 'Pawel987', 'karolina']
#current_users_copy = [word.lower() for word in current_users]
current_users_copy = []
for word in current_users:
	word = word.lower()
	current_users_copy.append(word)
print(current_users_copy)



new_users = ['luke1988', 'karolina', 'marzenka64', 'PAWEL987']
new_users_copy = [word.lower() for word in new_users]
print(new_users_copy)

for user in new_users_copy:

	if user in current_users_copy:
		print(f"Przykro nam ale nazwa {user}, jest już zajęta przez innego użytkownia. Wybierz inną.")
	else:
		print(f"Nazwa {user}, jest dostępna.")

