# Simple Mode
# Have the function SimpleMode(arr) take the array of numbers stored in arr and return the number that appears most frequently (the mode). For example: if arr contains [10, 4, 5, 2, 4] the output should be 4. If there is more than one mode return the one that appeared in the array first (ie. [5, 10, 10, 6, 5] should return 5 because it appeared first). If there is no mode return -1. The array will not be empty.
# Examples
# Input: [5,5,2,2,1]
# Output: 5
# Input: [3,4,1,6,10]
# Output: -1


solution:1

def most_frequent(arr):
    counter = [1, -1]  # counter[0] count of most frequent number, counter[1] number itself
    for i in arr:
        if arr.count(i) > counter[0]:
            counter[0] = arr.count(i)
            counter[1] = i

    return counter[1]

solution:2
def SimpleMode(arr):
  arr_num = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        arr_num.append(arr[i])

  return arr_num[0] if arr_num else -1

print(SimpleMode(input()))

solution:3
def SimpleMode(arr):
    from statistics import multimode
    if len(multimode(arr)) == len(arr):
        return -1
    else: 
        return multimode(arr)[0]
print(SimpleMode(input()))


solution:4
from collections import Counter
arr = [5,5,2,2,1]
counter_arr = Counter(arr)
print(counter_arr)
for i in arr:
    if arr.count(i) == max(counter_arr.values()):
        print(i)
        break
    else:
        print(-1)
