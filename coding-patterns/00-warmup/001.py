# Contain Duplicate (Easy)

class Solution:
    def containsDuplicate(self, nums):
      count = {}
      for num in nums:
        if num not in count.keys():
          count[num] = 0
        count[num] += 1

      for num in nums:
        if count[num] > 1:
          return True
          
      return False
