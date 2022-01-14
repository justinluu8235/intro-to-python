# /***********************************************************************
# Write a function `valuePair(obj1, obj2, key)` that takes in two objects
# and a key (string). The function should return an array containing the
# corresponding values of the objects for the given key.
# Examples:
# const object1 = {name: 'One', location: 'Remote', age: 1};
# const object2 = {name: 'Two', location: 'San Francisco'};
# valuePair(object1, object2, 'location'); // => [ 'Remote', 'San Francisco' ]
# valuePair(object1, object2, 'name'); // => [ 'One', 'Two' ]
# ***********************************************************************/

def valuePair(obj1, obj2, key):
    result = [obj1[key], obj2[key]]
    return result


object1 = {'name': 'One', 'location': 'Remote', 'age': 1}
object2 = {'name': 'Two', 'location': 'San Francisco'}

print(valuePair(object1, object2, 'location'))