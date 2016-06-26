def calc(num1,num2):
	r = num1 + num2
	print('%s + %s = %s' % (num1,num2,r))

numbers = {2:4, 3:9, 12:8}

for key,value in numbers.items():
	calc(key,value)
