# Swap II
# Have the function SwapII(str) take the str parameter and swap the case of each character. Then, if a letter is between two numbers (without separation), switch the places of the two numbers. For example: if str is "6Hello4 -8World, 7 yes3" the output should be 4hELLO6 -8wORLD, 7 YES3.
# Examples
# Input: "Hello -5LOL6"
# Output: hELLO -6lol5
# Input: "2S 6 du5d4e"
# Output: 2s 6 DU4D5E


def change(s,indx1,indx2):
  res=''
  for i in range(len(s)):
    if i== indx1:
      res += s[indx2]
    elif i== indx2:
      res += s[indx1]
    else:
      res += s[i]
  return res 

def tran(s):
  arr=[]
  for i in range(len(s)):  
    if s[i] in '0123456789':
      arr.append(i)
  if len(arr)<2:
    return s
  for i in range(arr[0]+1, arr[1]):
    if (s[i]>="a" and s[i]<="z") or (s[i]>="A" and s[i]<="Z"):
      return change(s, arr[0], arr[1])
  else:
    return s
  
def SwapII(str): 
  res=''
  for i in str:
    if i>="a" and i<="z":
      res += i.upper()
    elif i>="A" and i<="Z":
      res += i.lower()
    else:
      res +=i
  res1=res.split()
  lst=[]
  for i in range(len(res1)):
    lst.append(tran(res1[i]))
  return ' '.join(lst)



# keep this function call here 
print(SwapII(input()))
        
        