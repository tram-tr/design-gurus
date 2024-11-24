// Ceiling of a Number (Medium)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  static int searchCeilingOfANumber(const vector<int>& arr, int key) {
    if (key > arr[arr.size() -1]) 
        return -1;

    int start = 0; 
    int end = arr.size()-1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (key < arr[mid])
            end = mid - 1;
        else if (key > arr[mid])
            start = mid + 1;
        else
            return mid;
    }

    return start;
  }
};
