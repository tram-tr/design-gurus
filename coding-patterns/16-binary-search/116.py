# Ceiling of a Number (Medium)

class Solution:
  def searchCeilingOfANumber(self, arr, key):
    n = len(arr)
    if key > arr[n - 1]:  
      return -1

    start, end = 0, n - 1
    while start <= end:
      mid = start + (end - start) // 2
      if key < arr[mid]:
        end = mid - 1
      elif key > arr[mid]:
        start = mid + 1
      else:  
        return mid
      
    return start