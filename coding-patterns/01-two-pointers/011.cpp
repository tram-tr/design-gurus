// Find Non-Duplicate Number Instances (Easy)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  static int remove(vector<int> &arr) {
    int start = 0;
    int end = 1;
    int count = 0;
    while (start < arr.size()) {
      while (end < arr.size() && arr[end] == arr[start])
        end++;
      start = end;
      end++;
      count++;
    }
    return count;
  }
};