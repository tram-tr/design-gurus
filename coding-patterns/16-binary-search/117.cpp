// Next Letter (Medium)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  char searchNextLetter(const vector<char>& letters, char key) {
    int n = letters.size();
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (key < letters[mid])
            end = mid - 1;
        else 
            start = mid + 1;
    }

    return letters[start % n];
  }
};
