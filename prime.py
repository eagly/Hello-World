import math

def is_prime(number):
	y=int(math.sqrt(number))
	i=3
	if(number%2==0):
		return False
	else:
		while i<=y:
			if(number%i==0):
				return False
				break
				#i+=2
			else:
				i+=2		
	return True

def prime_list(number):
	plist=[]
	plist.append(2)
	plist.append(3)
	i=5
	while(i<number):
		for j in plist:
			if(int(math.sqrt(i))%j==0):
				break
		else:
			plist.append(i)
		i+=2
	return plist	
#for i in plist:
	#	print i,	
	
number=input('Enter a number: ')
#if(is_prime(number)):
#	print "This number is a prime"
#else:
#	print "This number is not a prime"

#i=3
#print "1 2",
#while i<number:
#	if(is_prime(i)):
#		print i,
#	i+=2
plist=prime_list(number)
for i in plist:
	print i,

