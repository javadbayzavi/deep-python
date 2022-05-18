import re
import time


def binarySearch(sortedlst , val):
    first = 0
    last = len(sortedlst) - 1
    index = -1
    while  (first < last) and (index == -1):
        mid = (last + first) // 2
        if sortedlst[mid] == val:
            return mid
        elif sortedlst[mid] < val:
            first = mid + 1
        else:
            last = mid - 1
    return index

lst = [1,2,3,5,6,8,9,12,34,56,76,87,90,99,123,43,56,456,876,987,1000]

start = time.time()
res = binarySearch(lst , 2)
end = time.time()
print(res)
print('result has found in :' + str(end - start))