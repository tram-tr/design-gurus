# Search in a Sorted Infinite Array (Medium)

import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


class Solution:
  def searchInfiniteSortedArray(self, reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
      newStart = end + 1
      end += (end - start + 1) * 2
      # increase to double the bounds size
      start = newStart

    return self.binary_search(reader, key, start, end)


  def binary_search(self, reader, key, start, end):
    while start <= end:
      mid = start + (end - start) // 2
      if key < reader.get(mid):
        end = mid - 1
      elif key > reader.get(mid):
        start = mid + 1
      else:  # found the key
        return mid

    return -1
