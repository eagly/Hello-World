import math, time

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
		if(is_prime(i)):
			#print i,
			plist.append(i)
		i+=2
	return plist

def plst(number):
        plist=[]
        plist.append(2)
        plist.append(3)
        i=5
        while(i<number):
                y=int(math.sqrt(i))
                for j in plist:
                        if(i%j==0):
                                break
                else:
                        #print i,
                        plist.append(i)
                i+=2
        return plist

def sieveOfErat(end):  
	if end < 2: return []  

	#The array doesn't need to include even numbers  
	lng = ((end/2)-1+end%2)  

	# Create array and assume all numbers in array are prime  
	sieve = [True]*(lng+1)  

	# In the following code, you're going to see some funky  
	# bit shifting and stuff, this is just transforming i and j  
	# so that they represent the proper elements in the array.  
	# The transforming is not optimal, and the number of  
	# operations involved can be reduced.  

	# Only go up to square root of the end  
	for i in range(int(math.sqrt(end)) >> 1):  

		# Skip numbers that aren't marked as prime  
		if not sieve[i]: continue  

		# Unmark all multiples of i, starting at i**2  
		for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
			sieve[j] = False  

	# Don't forget 2!  
	primes = [2]  

	# Gather all the primes into a list, leaving out the composite numbers  
	primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  

	return primes
	
	
number=input('Enter a number: ')
z=input('Enter 0 - Is prime \n \t1 - Prime list(is_prime) \n\t2 - Prime list normal \n\t3 - Sieve of Erat\n:')
start = time.time()

if(z==1):
	plist=prime_list(number)
	print "-------------------------------------"
	f = open('myfile.txt','w')
	f.write(str(plist).strip('[]'))
	f.close() 
elif (z==0):
	if(is_prime(number)):
		print "This number is a prime"
	else:
		print "This number is not a prime"
elif (z==2):
	plist=plst(number) 
	print "-------------------------------------"
        f = open('myfile.txt','w')
        f.write(str(plist).strip('[]')) # python will convert \n to os.linesep
        f.close()
else:
	plist=sieveOfErat(number) 
	print "-------------------------------------"
        f = open('myfile.txt','w')
        f.write(str(plist).strip('[]')) # python will convert \n to os.linesep
        f.close()
end = time.time()
print end - start
