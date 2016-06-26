#Takes in a first name and a last name, and prints out a full name, in a sentence
#call the function three times


def nome_a_caso (name, surname):

	full = (name + ' ' + surname)
	print('ciao %s' %full)

names = {'Roberto': 'Giallo', 'Bilbo':'Baggins', 'Sheldon':'Cooper'}

for name, surname in names.items():
	nome_a_caso(name,surname)

 
