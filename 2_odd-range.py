# /******************************************************************************
# Write a function oddRange(end) that takes in a number and returns an array 
# containing all positive odd numbers up to `end`.
# Examples:
# oddRange(13); // => [ 1, 3, 5, 7, 9, 11, 13 ]
# oddRange(6); // => [ 1, 3, 5 ]
# ******************************************************************************/

def oddRange(end):
    result = []
    for i in range(end+1):
        if(i % 2 == 1):
            result.append(i)

    return result

print(oddRange(6))
