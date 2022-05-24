# Task :
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
# "The hash() method returns the hash value of an object if it has one. Hash values are just integers that are used to compare dictionary keys during a dictionary look quickly."

# Input Format :
# The first line contains an integer, n, denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.

# Output Format :
# Print the result of hash(t).


# Sample Input :
# 2
# 1 2

# Sample Output :
# 3713081631934410656

# Solution :

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))



# Tutorial :
# Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot be modified once created). This restricts their use because we cannot add, remove, or assign values; however, it gives us an advantage in space and time complexities.

# A common tuple use is the swapping of 2 numbers:
# a, b = b, a

# Here a,b is a tuple, and it assigns itself the values of b,a.
# Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashable.

# tuple of vowels
# vowels = ('a', 'e', 'i', 'o', 'u')

# print('The hash is:', hash(vowels))
# The hash is: 4688563021877839830