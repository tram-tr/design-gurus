// Shortest Word Distance (Easy)

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
  int shortestDistance(vector<string>& words, string word1, string word2) {
    int shortestDistance = words.size();
    int position1 = -1, position2 = -1; 

    for (int i = 0; i < words.size(); i++) {
      string word = words[i];
      if (word == word1) {
        position1 = i;
      } else if (word == word2) {
        position2 = i;
      }
      if (position1 != -1 && position2 != -1) {
        shortestDistance = min(shortestDistance, abs(position1 - position2));
      }
    }
    return shortestDistance;
  }
};
