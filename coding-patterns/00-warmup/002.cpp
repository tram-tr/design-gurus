// Pangram (Easy)

#include<iostream>
#include<cctype>
#include<cstring>
#include <vector>
using namespace std;

class Solution {
  public:
    bool checkIfPangram(string sentence) {
      vector<int> counter(26, 0);
      for (int i = 0; i < sentence.length(); i++) {
        if (sentence[i] == ' ') continue;
        int c = tolower(sentence[i]) - 'a';
        counter[c]++;
      }

      for (auto c : counter) {
        if (c < 1) return false;
      }
      return true;
    }
};