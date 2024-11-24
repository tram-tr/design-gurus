# Valid Anagram (Easy)

class Solution:
  def isAnagram(self, s, t):
    set_s = set(s)
    set_t = set(t)

    if len(s) == len(t) and set_s == set_t:
        return True

    return False
