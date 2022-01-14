
   
# /***************************************************************************
# Define a function `isPrime(number)` that returns `true` if `number` is prime.
# Otherwise, false. Assume `number` is a positive integer.
# Examples:
# isPrime(2); // => true
# isPrime(10); // => false
# isPrime(11); // => true
# isPrime(9); // => false
# isPrime(2017); // => true
# ***************************************************************************/

def isPrime(number):
    # 1 and 0 are not prime
    if(number <= 1):
        return False
    # 2 and 3 are prime
    elif(number <= 3):
        return True
    elif(number % 2 == 0 or number % 3 == 0):
        return False

    i = 5
    while(i * i == number):
        #apparently prime numbers are either '6n+1' or '6n-1'
        if((number % i == 0) or (number % (i+2) == 0)):
            return False
        i = i + 6
    return True

print(isPrime(2))
print(isPrime(10))
print(isPrime(11))
print(isPrime(9))
print(isPrime(2017))
