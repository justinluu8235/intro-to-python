### Task 2


#Task 2-1
idx = 'abcde'.index('d')
idx = idx + 11
print('Task 2-1', idx)
idx * 2
print('Task 2-1', idx)


#Task 2-2
num=33
isEven = num % 2 == 0
print('Task 2-2', isEven)
print('Task 2-2', not isEven)

#Task 2-3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print('Task 2-3', num)
str2 = 'bootcamp'
print('Task 2-3', str2[num].upper())
char = str2[num].lower()
print('Task 2-3', char + '!')

#Task 2-4
sentence = 'welcome to bootcamp prep'
lastChar = sentence[len(sentence) - 1]
print('Task 2-4', lastChar)
print('Task 2-4', sentence.index(lastChar))



## Task 3


# Task 3-5
age = 30
if (age > 30):
    print('Task 3-5', 'older than 30')
else:
    print('Task 3-5', 'younger than 30')


# Task 3-6

str = 'pizza'
if(len(str) > 10):
    print('Task 3-6','long string')
else:
    print('Task 3-6','short string')
if(str[0] == 'p'):
    print('Task 3-6', 'starts with p')


# Task 3-7
num = 15
if(num % 3 == 0) :
    print('Task 3-7', 'divisible by 3')
elif(num % 5 == 0):
    print('Task 3-7', 'divisible by 5')


# Task 3-8
num = 15
if(num % 3 == 0):
    print('Task 3-8', 'divisble by 3')
if(num % 5 == 0):
    print('Task 3-8', 'divisible by 5')


# Task 3-9
str = 'General Assembly'
if(str[0] == str[0].upper()):
    print('Task 3-9' , 'starts with a capital!')
if(str[len(str) - 1] == str[len(str) - 1].upper()):
    print('Task 3-9' , 'ends with a capital!')


# Task 3-10 
num = -44
if(num > 0):
    print('Task 3-10 ', 'positive')
elif(num < 0):
    print('Task 3-10 ', 'negative')
else:
    print('Task 3-10 ', 0)

if(num % 2 == 0):
    print('Task 3-10 ', 'even' )
else:
    print('Task 3-10 ' , 'odd')


## Task 4

# Task 4-1
num = 11
if(num > 5):
    print('Task 4-1', 'if')

# Task 4-2
num = 5
if(num > 5):
    print('Task 4-2', 'if')
else:
    print('Task 4-2', 'else')


# Task 4-3
num = 0
if(num < 0):
    print('Task 4-3' , 'if')
elif(num > 0):
    print('Task 4-3', 'else if')
else:
    print('Task 4-3', 'else')


## Task 5

# Task 5-1
def say_hello(name):
    msg = f'Hello, {name}. How are you?'
    return msg

print('Task 5-1', say_hello('bootcam prep'))


# Task 5-2
def check_number(num):
    if(num > 0):
        return 'positive'
    elif(num < 0):
        return 'negative'
    else:
        return 'zero'
print('Task 5-2', check_number(5))

# Task 5-3
def fizz_buzz1(max):
    for i in range(max):
        if(i % 3 == 0 and i % 5 == 0):
            print('Task 5-3', i)
        elif(i % 5 ==0 and i % 3 != 0):
            print('Task 5-3', i)
fizz_buzz1(16)

# Task 5-4
def even_caps(sentence):
    new_sentence = ""
    for i in range(len(sentence)):
        char = sentence[i]
        if(i % 2 == 0):
            capitalChar = char.upper()
            new_sentence += capitalChar
        else:
            new_sentence += char
    return new_sentence

print(even_caps("hello world"))
        
