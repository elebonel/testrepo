#A list of desserts

desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
favorite_dessert = 'apple crisp'

for dessert in desserts:
	if dessert == favorite_dessert:
		print("%s is my favorite dessert!" % dessert.title() )
	else:
		print("I like %s." % dessert)
