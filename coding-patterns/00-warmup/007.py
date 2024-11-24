# Number of Good Pairs (Easy)

class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0
    map = {}
    for num in nums:
      map[num] = map.get(num , 0) + 1 
      pairCount += map[num] - 1
    return pairCount
