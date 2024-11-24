# Single Number (Easy)

class Solution:
    def findSingleNumber(self, arr):
        num = 0  
        for i in arr:
            num ^= i  # XOR operation to find the single number
        return num
