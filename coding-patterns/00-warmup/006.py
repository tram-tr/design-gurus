# Shortest Word Distance (Easy)

class Solution:
  def shortestDistance(self, words, word1, word2):
    # TODO: Write your code here
    idx1, idx2 = -1, -1
    dist = len(words)
    for i in range(len(words)):
      if words[i] == word1:
        idx1 = i
      if words[i] == word2:
        idx2 = i 

      if idx1 != -1 and idx2 != -1:
        dist = min(abs(idx1-idx2), dist)

    return dist
