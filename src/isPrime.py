#  Given a number provided by the command line determine if it is a prime number

import getopt, sys 
  
argumentList = sys.argv[1:] 
  
options = "hmo:"
  
long_options = ["Number"] 

number = 0

def isPrime(p):
    if p > 1:
        for i in range(2, p // 2):
            if (p % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False
    
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
