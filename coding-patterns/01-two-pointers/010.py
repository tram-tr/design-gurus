# Pair with Target Sum (Easy)

class Solution:
  def search(self, arr, target_sum):
    left, right = 0, len(arr) - 1
    while(left < right):
      current_sum = arr[left] + arr[right]
      if current_sum == target_sum:
        return [left, right]

      if target_sum > current_sum:
        left += 1  
      else:
        right -= 1 
    return [-1, -1]