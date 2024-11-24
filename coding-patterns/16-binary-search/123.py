# PC 2: Search in Rotated Array (Medium)

class Solution:
  def search(self, arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
      mid = start + (end - start) // 2
      if arr[mid] == key:
        return mid

      if arr[start] <= arr[mid]:  # left side is sorted in ascending order
        if key >= arr[start] and key < arr[mid]:
          end = mid - 1
        else:  # key > arr[mid]
          start = mid + 1
      else:  # right side is sorted in ascending order
        if key > arr[mid] and key <= arr[end]:
          start = mid + 1
        else:
          end = mid - 1

    return -1


