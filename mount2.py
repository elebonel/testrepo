mountains = {'Everest':[8848,29029],'K2':[8611, 28251],'Kang':[8586,28169],'Lhotse': [8516,27940], 'kalu':[8462,27762]}


print('The name of the highest mountains in the world is:')
for mountain in mountains.keys():
        print('\n')
        print(mountain)


print('The height of the highest mountains in the world is:')
for mountain in mountains.values():
        print('\n')
        print(mountain[0])
for mountain in mountains.values():
        print('\n')
        print(mountain[-1])

print('sentences on mountains:')
for name,height in mountains.items():
        print('\n')
        print('%s is %s metres tall,or %s feet' %(name,height[0], height[-1]))


