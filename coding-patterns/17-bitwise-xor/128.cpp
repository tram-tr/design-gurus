// Flip and Invert an Image

#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>> arr) {
      int s = arr[0].size(); // Get the size of each row (assuming all rows have the same size)
      for (int row = 0; row < arr.size(); row++) { // Iterate through each row in the matrix
          for (int col = 0; col < (s + 1) / 2; ++col) { // Iterate through the first half of each row
              int tmp = arr[row][col] ^ 1; // Invert the current element and store it in 'tmp'
              arr[row][col] = arr[row][s - 1 - col] ^ 1; // Invert and swap elements symmetrically from the beginning and end of the row
              arr[row][s - 1 - col] = tmp; // Set the swapped element to 'tmp'
          }
      }
      return arr; // Return the modified matrix
    }
};
