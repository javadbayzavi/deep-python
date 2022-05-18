
import time
from numpy import inner


def bubbleSOrt(lst):
    if len(lst) <= 1:
        return lst
    for outr in range(len(lst) - 1,0,-1):
        for iner in range(outr):
            if lst[iner] > lst[iner + 1]:
                tempp = lst[iner]
                lst[iner] = lst[iner+1]
                lst[iner+ 1] = tempp

lst = [22,54,8,12,9,56,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,1,45,267,3,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,6,2,5,7,39,7,4,7,39,7,4,22,54,8,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4]
start = time.time()
bubbleSOrt(lst)
end = time.time()
print(lst)
print(end - start)