# Minimum Difference Element (Medium)

class Solution:
  def searchMinDiffElement(self, arr, key):
    if key < arr[0]:
      return arr[0]
    n = len(arr)
    if key > arr[n - 1]:
      return arr[n - 1]

    start, end = 0, n - 1
    while start <= end:
      mid = start + (end - start) // 2
      if key < arr[mid]:
        end = mid - 1
      elif key > arr[mid]:
        start = mid + 1
      else:
        return arr[mid]

    if (arr[start] - key) < (key - arr[end]):
      return arr[start]
    return arr[end]