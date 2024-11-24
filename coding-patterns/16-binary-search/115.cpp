// Order-agnostic Binary Search (Easy)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  int search(const vector<int>& arr, int key) {
    int start = 0;
    int end = arr.size()-1;
    bool ascending = arr[start] < arr[end];

    while (start <= end) {
      int mid = start + (end - start) / 2;

      if (key == arr[mid])
        return mid;

      if (ascending) {
        if (key < arr[mid])
          end = mid - 1;
        else
          start = mid + 1;
      } else {
        if (key > arr[mid])
          end = mid - 1;
        else
          start = mid + 1;
      }
    }
    return -1; 
  }
};
