# /***********************************************************************
# Write a function `doesKeyExist(obj, key)` that takes in an object and a
# key and returns true if the key is inside the object and false if the
# key is not inside the object.
# Examples:
# const obj1 = {company: 'General Assembly', course: 'Software Engineering Immersive'}
# doesKeyExist(obj1, 'company'); // => true
# doesKeyExist(obj1, 'name'); // => false
# ***********************************************************************/

def doesKeyExist(obj, key):
    if(obj.get(key)):
        return True
    else:
        return False


obj1 = {'company': 'General Assembly', 'course': 'Software Engineering Immersive'}
print(doesKeyExist(obj1, 'name'))