// Valid Palindrome (Easy)

#include <iostream>

class Solution {
public:
  bool isPalindrome(std::string s) {
    // TODO: Write your code here
    int start = 0;
    for (int end = s.length()-1; end >= 0; end--) {
      if (start < end && isalnum(s[end])) {
        while (start < end && !isalnum(s[start]))
          start++;
        if (tolower(s[start]) != tolower(s[end]))
          return false;
        start++;
      }
    }
    return true;
  }
};
