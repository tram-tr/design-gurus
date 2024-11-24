# Find Non-Duplicate Number Instances (Easy)

class Solution:
  def moveElements(self, arr):
    next_non_duplicate = 1

    i = 0
    while i < len(arr):
      if arr[next_non_duplicate - 1] != arr[i]:
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
      i += 1

    return next_non_duplicate