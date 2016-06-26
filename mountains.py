mountains = {'Everest':'8848', 'K2': '8611', 'Kang':'8586', 'Lhotse': '8516', 'Makalu':'8462'} 


print('The name of the highest mountains in the world is:')
for mountain in mountains.keys():
	print('\n')
	print(mountain)

print('The height of the highest mountains in the world is:')
for mountain in mountains.values():
	print('\n')	
	print(mountain)


print('sentences on mountains:')
for name,height in mountains.items():
	print('\n')
	print('%s is %s metres tall' %(name,height))


