mountains = {'Everest':{'height':'8848','range':'Himalaya'}, 'k2':{'height':8611,'range':'Karakora'}, 'kanchenjunga':{'height':8586,'range':'himalaya'}, 'lthose':{'height':8516,'range':'himalaya'}, 'makalu':{'height':8463,'range':'himalaya'}}


print('The name of the highest mountains in the world is:')
for mountain in mountains.keys():
        print('\n')
        print(mountain)


print('The height of the highest mountains in the world is:')
for mountain in mountains.values():
        print('\n')
        print(mountain['height'])
for mountain in mountains.values():
        print('\n')
        print(mountain['range'])

print('sentences on mountains: ')
for name,height in mountains.items():
        print('\n')
        print('%s is a %s metres tall mountain in the %s range' %(name,height['height'], height['range']))



