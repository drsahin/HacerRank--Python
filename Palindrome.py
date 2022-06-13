# Palindrome
# Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string.
# Examples
# Input: "never odd or even"
# Output: true
# Input: "eye"
# Output: true

def Palindrome(str):
  liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  a = ""
  for i in str :
    if i in liste :
      a +=i
  if a == a[::-1] :
    return True
  else: 
    return False
    

# keep this function call here 
print(Palindrome(input()))


solution:2

def Palindrome(strParam):

  # code goes here
  strParam = ''.join(strParam.split())
  return strParam == strParam[::-1]

# keep this function call here
print(Palindrome(input()))