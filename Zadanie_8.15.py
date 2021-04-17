#Import modułów z funkcjami
import printing_functions as p


#Wczytanie list z modelami i wykonanymi modelami
unprinted_desings = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_models = []

#Wywołanie funckji
p.print_models(unprinted_desings, completed_models)
p.show_completed_models(completed_models)