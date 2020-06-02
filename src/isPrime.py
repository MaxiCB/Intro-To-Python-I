#  Given a number provided by the command line determine if it is a prime number

import getopt, sys 
from math import sqrt
  
argumentList = sys.argv[1:] 
  
options = "hmo:"
  
long_options = ["Number"] 

number = 0

# A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
def isPrime(p):
    # Prime cannot be negative, or 1
    if(p <= 1):
        return False
    # 2&&3 are both primes
    if(p <= 3): 
        return True
    # If number is divisible by 2||3 it is not prime
    if( p % 2 == 0 or p % 3 == 0):
        return False
    # This  above logic handles primes up until 23
    
    # This logic handles 29+ 
    # Initially set i to next possible prime
    i = 5
    # while i * i <=p
    while(i * i <= p):
        # Check if remainder of p%i\\p%i+1 is 0
        if(p % i == 0 or p % (i + 2) == 0):
            return False
        i = i + 6
    return True
    
try: 
    arguments, values = getopt.getopt(argumentList, options, long_options) 
      
    for currentArgument, currentValue in arguments: 
  
        if currentArgument in ("-n", "--Number"):
            number = sys.argv[2]
            if(isPrime(int(number))):
                print(number, 'is a prime number')
            else:
                print(number, 'is not a prime number')
              
except getopt.error as err: 
    print (str(err))
