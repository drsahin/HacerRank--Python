# Nim Winner
# Have the function NimWinner(arr) take the array of integers stored in arr which will represent the amount of coins in each pile. For example: [2, 4, 1, 3] means there are 4 piles of coins and there are 2 coins in the first pile, 4 in the second pile, etc. Nim is played by each player removing any number of coins from only one pile, and the winner is the player who picks up the last coin. For example: if arr is [1, 2, 3] then for example player 1 can remove 2 coins from the last pile which results in [1, 2, 1]. Then player 2 can remove 1 coin from the first pile which results in [0, 2, 1], etc. The player that has the last possible move taking the last coin(s) from a pile wins the game. Your program should output either 1 or 2 which represents which player has a guaranteed win with perfect play for the Nim game.
# Examples
# Input: [1,2,3]
# Output: 2
# Input: [1,1,1,4,5,4]
# Output: 1

solution:1

def NimWinner (arr):
  isPlayer1 = 2
  newArr = findNumberIndex(arr)
  while newArr[0] > 0 or newArr[1] > 0 or newArr[2] > 0:
    if newArr[2] > 0 and  newArr[2]%2==0:
      newArr[2]-=1
    elif newArr[1] > 0 and newArr[1]%2==0:
      newArr[1]-=1
    elif newArr[0] > 0 and newArr[0]%2==0:
      newArr[0]-=1
    elif newArr[2] > 0:
      newArr[2]-=1
    elif newArr[1] > 0:
      newArr[1]-=1
    elif newArr[0] > 0:
      newArr[0]-=1
    isPlayer1 = 1 if isPlayer1 == 2 else 2
    
  return isPlayer1

def findNumberIndex (arr):
  four = 0
  two = 0
  one = 0
  i = 0
  while i < len(arr):
    if arr[i] - 3 == 4:
      four+= 1
      two+= 1
      one+= 1
    if arr[i] - 2 == 4:
      four+= 1
      two+= 1
    elif arr[i] - 1 == 4:
      four+= 1
      one+= 1
    elif arr[i] == 4:
      four+= 1
    elif arr[i] - 1 == 2:
      two+= 1
      one+= 1
    elif arr[i] == 2:
      two+= 1
    elif arr[i] == 1:
      one+= 1
    i += 1
  return [one,two,four]



solution:2

def new_piles(arr):

  coppied_arr = [i for i in arr]
  # print("coppied_arr:", coppied_arr)

  if sum(coppied_arr)  <= 3 or len(coppied_arr) < 2:
    return coppied_arr
  else:
    for i in range(len(arr)):
      coppied_arr[i] -= arr[0]

    if len(coppied_arr) > 1:
      coppied_arr.pop(0)
    
    return new_piles(coppied_arr)


def NimWinner(arr):

  if len(arr) > 1:
    arr.sort()
    new_arr = new_piles(arr)
    
    return 1 if new_arr[0] % 3 == 0 else 2
  else:
    return 1 if new_arr[0] % 3 == 0 else 2

# keep this function call here 
print NimWinner(raw_input())
