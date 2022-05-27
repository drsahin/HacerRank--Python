# Vowel Count
# Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge.
# Examples
# Input: "hello"
# Output: 2
# Input: "coderbyte"
# Output: 3

# Solution:

def VowelCount(strParam):
  num_wowels=0
  for i in strParam :
    if i in "aeiouAEIOU" :
      num_wowels += 1
  # code goes here
  return num_wowels

# keep this function call here 
print VowelCount(raw_input())