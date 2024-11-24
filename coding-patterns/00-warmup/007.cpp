// Number of Good Pairs (Easy)

#include <iostream>
#include <map>
#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
  public:
    int numGoodPairs(std::vector<int>& nums) {
      int pairCount = 0;
      std::unordered_map<int, int> hmap;
      for (auto num : nums) {
        hmap[num];
        hmap[num]++;
        pairCount += hmap[num] - 1;
      }
      return pairCount;
    }
};
