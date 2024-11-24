# PC 1: Search Bitonic Array (Medium)

class Solution:
  def search(self, arr, key):
    maxIndex = self.find_max(arr)
    keyIndex = self.binary_search(arr, key, 0, maxIndex)
    if keyIndex != -1:
      return keyIndex
    return self.binary_search(arr, key, maxIndex + 1, len(arr) - 1)


  # find index of the maximum value in a bitonic array
  def find_max(self, arr):
    start, end = 0, len(arr) - 1
    while start < end:
      mid = start + (end - start) // 2
      if arr[mid] > arr[mid + 1]:
        end = mid
      else:
        start = mid + 1

    return start

  def binary_search(self, arr, key, start, end):
    while start <= end:
      mid = int(start + (end - start) / 2)

      if key == arr[mid]:
        return mid

      if arr[start] < arr[end]:  # ascending order
        if key < arr[mid]:
          end = mid - 1
        else:  # key > arr[mid]
          start = mid + 1
      else:  # descending order
        if key > arr[mid]:
          end = mid - 1
        else:  # key < arr[mid]
          start = mid + 1

    return -1  

