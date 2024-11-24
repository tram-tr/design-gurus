# Pangram (Easy)

class Solution:
  def checkIfPangram(self, sentence):
    '''letters = 'abcdefghijklmnopqrstuvwxyz'
    count = {}
    for c in letters:
      count[c] = 0

    for i in range(len(sentence)):
      if sentence[i].isalpha():
        count[sentence[i].lower()] += 1

    for c in letters:
      if count[c] < 1:
        return False

    return True'''

    seen = set()

    for c in sentence.lower():
      if c.isalpha():
        seen.add(c)

    if len(seen) == 26:
      return True

    return False
