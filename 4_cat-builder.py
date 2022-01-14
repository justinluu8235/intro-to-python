
   
# /***********************************************************************
# Write a function `catBuilder(name, color, toys)` that returns a cat object
# object with the corresponding properties.
# Example:
# const cat1 = catBuilder('Garfield', 'golden', ['scratching-post', 'yarn']);
# cat1; // => { name: 'Garfield', color: 'golden', toys: ['scratching-post', 'yarn'] }
# const cat2 = catBuilder('Whiskers', 'rainbow', ['poptarts']);
# cat2; // => { name: 'Whiskers', color: 'rainbow', toys: [ 'poptarts' ] }
# ***********************************************************************/

def catBuilder(name, color, toys):
    result = {}
    result["name"] = name
    result["color"] = color
    result["toys"] = toys
    return result

cat1 = catBuilder('Garfield', 'golden', ['scratching-post', 'yarn'])
print(cat1)

