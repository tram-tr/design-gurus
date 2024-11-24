# PC 3: Rotation Count (Medium)

class Solution:
  def countRotations(self, arr):
    start, end = 0, len(arr) - 1
    while start < end:
      mid = start + (end - start) // 2

      if mid < end and arr[mid] > arr[mid + 1]:
        return mid + 1
      if mid > start and arr[mid - 1] > arr[mid]:
        return mid

      if arr[start] < arr[mid]:  
        start = mid + 1
      else: 
        end = mid - 1

    return 0  
