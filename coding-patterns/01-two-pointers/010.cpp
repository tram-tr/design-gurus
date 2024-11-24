// Pair with Target Sum (Easy)

using namespace std;

#include <iostream>
#include <vector>

class Solution {

  public:

  static vector<int> search(const vector<int> &arr, int targetSum) {
    // TODO: Write your code here
    int start = 0;
    for (int end = arr.size() - 1; end > -1; end--) {
      while (start < end && arr[start] + arr[end] < targetSum)
        start++;
      if (start != end && arr[start] + arr[end] == targetSum) {
        return vector<int>{start, end};
      }
    }
    return vector<int>(2, -1);
  }

};
