# /***********************************************************************
# In these exercises we will be practicing decomposition by building
# multiple functions. Be sure to test each function thoroughly as you go
# before moving on to the next problem. Each function will require the
# previous to solve.
# ***********************************************************************/


# /***********************************************************************
# Write a function `isPrime(number)` that returns a boolean indicating if
# `number` is prime or not. Assume `number` is a positive integer.
# Examples:
# isPrime(2); // => true
# isPrime(1693); // => true
# isPrime(15); // => false
# isPrime(303212); // => false
# ***********************************************************************/

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
# /***********************************************************************
# Using the `isPrime` function you made, write a function `firstNPrimes(n)`
# that returns an array of the first `n` prime numbers.
# Examples:
# firstNPrimes(0); // => []
# firstNPrimes(1); // => [2]
# firstNPrimes(4); // => [2, 3, 5, 7]
# ***********************************************************************/

def firstNPrimes(n):
    result = []
    if(n == 0): return result
    for i in range(100):
        if(isPrime(i)):
            result.append(i)
            if(len(result) == n):
                break

    return result

print(firstNPrimes(0))
print(firstNPrimes(1))
print(firstNPrimes(4))
# /***********************************************************************
#  Using `firstNPrimes`, write a function `sumOfNPrimes(n)` that returns
# the sum of the first `n` prime numbers.
# Examples:
# sumOfNPrimes(0); // => 0
# sumOfNPrimes(1); // => 2
# sumOfNPrimes(4); // => 17
# ***********************************************************************/

def sumOfNPrimes(n):
    array = firstNPrimes(n)
    sum = 0
    for i in array:
        sum += i
    return sum

print(sumOfNPrimes(0))
print(sumOfNPrimes(1))
print(sumOfNPrimes(4))

