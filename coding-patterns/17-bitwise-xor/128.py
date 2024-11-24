# Flip and Invert an Image (Hard)

class Solution:
  def flipAndInvertImage(self, matrix):
    C = len(matrix[0])  # Get the number of columns in the matrix
    for row in matrix:
      for i in range((C+1)//2):  # Iterate through the first half of the row
        # Swap and invert elements symmetrically from the beginning and end of the row
        row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
        
    return matrix
