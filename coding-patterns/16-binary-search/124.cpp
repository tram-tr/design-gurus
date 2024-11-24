// PC 3: Rotation Count (Medium)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  int countRotations(const vector<int>& arr) {
    int start = 0, end = arr.size() - 1;
    while (start < end) {
      int mid = start + (end - start) / 2;

      if (mid < end && arr[mid] > arr[mid + 1])  
        return mid + 1;
      
      
      if (mid > start && arr[mid - 1] > arr[mid]) 
        return mid;
      

      if (arr[start] < arr[mid]) 
        start = mid + 1;
      else   
        end = mid - 1;
      
    }

    return 0;  
  }
};
