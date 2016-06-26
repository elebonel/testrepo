def calc(num1,num2):
        r = num1 + num2
	return r 

numbers = {2:4, 3:9, 12:8}

for key,value in numbers.items():
        n = calc(key,value)
	print('%s + %s = %s' % (key,value,n))




