// Single Number (Easy)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
  public:
    int findSingleNumber(const vector<int>& arr) {
      int num = 0;
      for (int i=0; i < arr.size(); i++) {
        num = num ^ arr[i];  // XOR operation to find the single number
      }
      return num;
    }
};

