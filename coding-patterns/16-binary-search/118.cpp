// Number Range (Medium)

using namespace std;

#include <iostream>
#include <vector>

class Solution {
public:
  vector<int> findRange(const vector<int> &arr, int key) {
    vector<int> result(2, -1);
    result[0] = search(arr, key, false);

    if (result[0] != -1)
        result[1] = search(arr, key, true);

    return result;
  }

private:
    static int search(const vector<int> &arr, int key, bool maxid) {
        int keyid = -1;
        int start = 0;
        int end = arr.size() - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (key < arr[mid])
                end = mid - 1;
            else if (key > arr[mid])
                start = mid + 1;
            else {
                keyid = mid;
                if (maxid)
                    start = mid + 1;
                else 
                    end = mid - 1;
            }
        }

        return keyid;
    }

};
