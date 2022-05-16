# Problem Statement :
    
# Consider a list (list = []). You can perform the following commands:
# 1.insert i e: Insert integer e at position i.
# 2.print: Print the list.
# 3.remove e: Delete the first occurrence of integer e.
# 4.append e: Insert integer e at the end of the list.
# 5.sort: Sort the list.
# 6.pop: Pop the last element from the list.
# 7.reverse: Reverse the list.

# Initialize your list and read in the value n of followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Input Format :
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints :
# The elements added to the list must be integers.

# Output Format :
# For each command of type print, print the list on a new line.

# Sample Input :
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output :
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

# Solution :

list = []
if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(0,N):
        cmd=input().split()
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort()
        else:
            L.reverse()





# Tutorial :
# When we talk about storing multiple values in a container-like data structure, the first thing that comes to mind is a list.
# You can initialize a list as:
# arr = list()
# # or simply
# arr = []

# or with a few elements as:
# arr = [1,2,3]

# Elements can be accessed easily similar to most programming languages:
# print arr[0]
# # result is 1
# print arr[0] + arr[1] + arr[2]
# # result is 6

# Lists in Python are very versatile. You can add almost anything in a Python list.
# In Python, you can create a list of any objects: strings, integers, or even lists. You can even add multiple types in a single list!
# Let's look at some of the methods you can use on list.

# 1.) append(x)
# Adds a single element x to the end of a list.
# arr.append(9)   
# print arr  
# # prints [1, 2, 3, 9]

# 2.) extend(L)
# Merges another list L to the end.
# arr.extend([10,11])
# print arr
# # prints [1, 2, 3, 9, 10, 11]

# 3.) insert(i,x)
# Inserts element x at position i.
# arr.insert(3,7)
# print arr
# # prints [1, 2, 3, 7, 9, 10, 11]

# 4.) remove(x)
# Removes the first occurrence of element x.
# arr.remove(10)  
# arr  
# # prints [1, 2, 3, 7, 9, 11]

# 5.) pop()
# Removes the last element of a list. If an argument is passed, that index item is popped out.
# temp = arr.pop()
# print temp 
# # prints 11

# 6.) index(x)
# Returns the first index of a value in the list. Throws an error if it's not found.
# temp = arr.index(3)
# print temp
# # prints 2

# 7.) count(x)
# Counts the number of occurrences of an element x.
# temp = arr.count(1)
# print temp
# # prints 1

# 8.) sort()
# Sorts the list.
# arr.sort()
# print arr
# # [1, 2, 3, 7, 9]

# 9.) reverse()
# Reverses the list.
# arr.reverse()
# print arr
# # [9, 7, 3, 2, 1]