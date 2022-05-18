from operator import le
import re
import time


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    middle = len(lst) // 2
    lefhalf = lst[: middle]
    righthalf = lst[middle:]
    leftlist = merge_sort(lefhalf)
    rightlist = merge_sort(righthalf)
    return mergList(leftlist , rightlist)

def mergList(left, right):
    result = []
    while (len(left) > 0) and (len(right) > 0):
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result


lst = [22,54,8,12,9,56,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,1,45,267,3,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,6,2,5,7,39,7,4,7,39,7,4,22,54,8,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4]
start = time.time()
resutl = merge_sort(lst)
end = time.time()
print(resutl)
print(end - start)