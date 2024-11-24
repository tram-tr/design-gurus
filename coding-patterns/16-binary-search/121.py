# Bitonic Array Maximum (Easy)

class Solution:
  def findMax(self, arr):
    start, end = 0, len(arr) - 1
    while start < end:
      mid = start + (end - start) // 2
      if arr[mid] > arr[mid + 1]:
        end = mid
      else:
        start = mid + 1

    # at the end of the while loop, 'start == end'
    return arr[start]
