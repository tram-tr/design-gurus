# Number Range (Medium)

class Solution:
  def findRange(self, arr, key):
    result = [- 1, -1]
    result[0] = self.binary_search(arr, key, False)
    if result[0] != -1:
      result[1] = self.binary_search(arr, key, True)
    return result


  # modified Binary Search
  def binary_search(self, arr, key, findMaxIndex):
    keyIndex = -1
    start, end = 0, len(arr) - 1
    while start <= end:
      mid = start + (end - start) // 2
      if key < arr[mid]:
        end = mid - 1
      elif key > arr[mid]:
        start = mid + 1
      else: 
        keyIndex = mid
        if findMaxIndex:
          start = mid + 1  
        else:
          end = mid - 1 

    return keyIndex
