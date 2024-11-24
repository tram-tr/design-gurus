// Valid Anagram (Easy)

#include <iostream>
#include <unordered_map>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
      if (s.length() != t.length())
        return false;
      
      std::unordered_map<char, int> freqMap;
      for (int i = 0; i < s.length(); i++) {
        freqMap[s[i]]++;
        freqMap[t[i]]--;
      }

      for (const auto& [chr, freq] : freqMap) {
        if (freq != 0) return false;
      }
      
      return true;
    }
};