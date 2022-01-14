# # this is a comment 
# # TODO build this function

# def add(num1, num2):
#     '''
#     this is a multiline comment.
#     This function is to add 2 numbers
#     '''


# name = "Johnny"
# print(name)

# nothing = None
# print(nothing)

# is_working = True
# car_off = False


# if nothing: 
#     print('This is true')
#     num=7
#     print('car is off')
# elif car_off:
#     print("this is the second condition")
# elif is_working:
#     print("this is working")
# else:
#     print('This is not true..')

# #separate conditional
# if is_working:
#     print('this is working also')


# ## IN GENERAL, python waits for each line of code to run before the next. javascript does it at the same time unless async await is used

# print(15/6)
# print(15//6) # the '//' forces the result into a integer


# #Javascript : Math.pow(2, 3)
# #Python: 2 ** 3 

# # => ["ace", "of", "spades"]
# print('ace of spades'.split(" "))

# #split into individual characters
# print(list('aceofspades'))

# #finds first index of l
# print("hello".index("l"))

# #check if substring is in a string; a conditional
# print( "eggs" in "green eggs and ham")

# # check length of string
# print(len("Food"))

# print("my code rulez" [-1])
# print("my code rulez" [3:7])
# print("my code rulez" [:7])
# print("my code rulez" [3:])
# #reverse order
# print("my code rulez" [::-1])
# #take every other letter
# print("peiege eleaeteiene"[::2])



# if(not 7):
#     print("This is 7")
# else:
#     print("This is the second condition")




# ##### LISTS

# arr = [1, "two", 3, "four", True, False, "hello"]
# print(len(arr))
# print(arr[1])
# print(arr[-1])

# one_through_ten = list(range(10))
# print(one_through_ten)
# three_through_ten = list(range(3,10))
# print(three_through_ten)

# #sort
# a = [1,23,12, 99,82]
# a.sort()
# print(a)

# #reverse
# a = a[::-1]
# print(a)

# #add to end 
# a.append(88)
# print(a)

# #remove from end 
# popped = a.pop()
# print(a)
# print(popped)


# a.insert(1,77)
# print('After inserting 77 at index 1', a)

# if 23 in a :
#     print('This is michael jordan number')


# print('7'.isdigit())

### Dictionaries
# cat = {
#   "name": [1,2,3],
#   "breed": 'American Shorthair',
#   "fav_food": 'Prosciutto'
# }

# print(cat["name"])
# print(cat.get("fav_food"))
# cat['age'] = 30
# print(cat.get('age'))
# print(cat.items())
# print(cat.keys())
# print(cat.values())

# cat_keys = list(cat.keys())
# print(cat_keys[0])



##Type conversion
# print(int("42"))
# print(float(42))
# print(bool(42))
# print(bool(""))


## String interpolation
# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)

# topic = 'Inflation'
# num = 7
# y = 1982
# my_second_message = "{} is at at {} percent. Highest since {}".format(topic, num, y)
# print(my_second_message)

# template = 'My name is {name} and I like {food}'
# print(template)
# print(template.format(food="Chinese", name="Steve"))


# ## Function
# def st_nd_rd_th(n):
#   # add one to 13 because range is exclusive at the end.
#   if n in range(11, 13 + 1):
#     return "th"
#   if n % 10 == 1:
#     return "st"
#   elif n % 10 == 2:
#     return "nd"
#   elif n % 10 == 3:
#     return "rd"
#   else:
#     return "th"

# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
# print(my_message)



# # Loops
# n = 0
# while n < 100:
#     n += 1
#     if n%2==0:
#         print(f'{n} is even...')


# for i in range(0,10):
#     if i % 2 ==0:
#         print("{} is even".format(i))
#     if i % 2 ==1:
#         print("{} is odd".format(i))


# n= True
# num = 1
# while n:
#     if num % 2  == 0:
#         print(f'{num} is even')

#         if num == 750:
#             n=False
#             print('End Program')
#     num += 1


# #for loop
# for i in range(1,751):  #if wanted to increment by 3, range(1,751,3)
#     if( i % 2 ==0):
#         print(f'{i} is even')
        
#         if( i == 750): 
#             print('End Program')


# nums = [1,2,3,55,66,44,33,22,11,33,44]
# for i in range(len(nums)):
#     element = nums[i]
#     print(element)


students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    },
     { 
        "name": "John",
        "city": "Atlanta"
    },
    { 
        "name": "Jane",
        "city": "New York"
    },
    { 
        "name": "Rob",
        "city": "Los Angeles"
    },
     { 
        "name": "Harper",
        "city": "Washington"
    },
    { 
        "name": "Mike",
        "city": "Seattle"
    },
    { 
        "name": "Set",
        "city": "San Francisco"
    },
]

# for i in range(len(students)):
#     student = students[i]
#     print(student.get("name"))
#     print(student.get("city"))
#     if(student.get("city") == 'Los Angeles'):
#         print(f'{student.get("name")} wins an iPad for {student.get("city")}')



# # Iterating through without index
# for student in students:
#     print (student)

# # Iterating through a dictionary
# for key in students[0]:
#     print(key)
#     print('Value', students[0].get(key))

# # Iterating through a dictionary part 2
# for key, value in students[0].items():
#     print(key, '->', value)




# foods = ["carrots", "kale", "beets"]
# for i, food in enumerate(foods):
#   print("{}. {}".format(i, food))


# def say_hello(friend="Tim"):
#   print("Hello, {}!".format(friend))


# say_hello("Tom")

# def move(name, city="Seattle", state="Washington"):
#   msg = "{} is moving to {}, {}"
#   msg = msg.format(name, city, state)
#   print(msg)

# move("Charlie", "Los Angeles", "California")
# move(city="San Fransisco", name="Mark", state="California")
# move("John", state="New York", city="New York")


# def say_bye(name1, name2):
#     print(f'{name1} said hi to {name2}')

# say_bye("justin", "john")

def get_cities(students):
    '''Return a list of all cities from the student array'''
    result = []
    for s in students:
        if s.get('city') and s.get('city') not in result:
            result.append(s.get('city'))

    return result

def get_names(students):
    '''Return a list of all names from the student array'''
    result = []
    for s in students:
        if s.get('name'):
            result.append(s.get('name'))

    return result


print(get_cities(students))
print(get_names(students))


def parse_by_cities(students):
    '''
    Return a dictionary that has a key for each cities 
    and a list of students for each city 
    '''
    result = {}
    for student in students: 
        # if city is not in the dictionary, add the city and set an array with the
        if(student.get('city')):
            city = student.get('city')
            if not result.get(city):
                result[city] = [student.get('name')]
            # if city is in the dictionary, append student name 
            else:
                result[city].append(student.get('name'))

    return result

print( parse_by_cities(students))