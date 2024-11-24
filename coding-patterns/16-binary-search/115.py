# Order-agnostic Binary Search (Easy)

class Solution:
  def search(self, arr, key):
    start, end = 0, len(arr) - 1
    ascending = arr[start] < arr[end]
    while start <= end:
      mid = start + (end - start) // 2

      if key == arr[mid]:
        return mid

      if ascending:  
        if key < arr[mid]:
          end = mid - 1  
        else:  
          start = mid + 1 
      else: 
        if key > arr[mid]:
          end = mid - 1  
        else:  
          start = mid + 1  

    return -1  

