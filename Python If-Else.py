# Task
# Given an integer, n , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# A single line containing a positive integer, n.

# Constraints
# 1<= n <= 100
# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird

# Explanation 0
# n=3
# n is odd and odd numbers are weird, so print Weird.

# Sample Input 1
# 24
# Sample Output 1
# Not Weird

# Explanation 1
# n=24
# n>20 and n is even, so it is not weird.
 
# code1:

n = int(input())
if  5>= n >= 2 :
    if n % 2 == 0 :
        print("Not Weird")
if 20 >= n >= 6 :
    if n % 2 == 0 or n%2 == 1 :
        print("Weird")
if n > 20 :
    if n % 2 == 0 :
        print("Not Weird")         
if n % 2 == 1 or n == 1 :
  print("Weird")
  

# code2:

n = int(input().strip())

if n%2 != 0:
    print("Weird")
else :
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")