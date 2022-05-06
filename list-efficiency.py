import heapq
from collections import deque
from bisect import bisect, bisect_left
from queue import PriorityQueue
import timeit

from numpy import sort
simplelist =  [1,2,3,4,5,6,7,8,9,44,12,65,17,24,697,235,786,26,8,3,7]


xlist = deque(simplelist)
#append to the start of a list
xlist.appendleft(12)
sorted = sort(simplelist)
print(sorted)

#using binsect in ordered list to quickly find the positions
print(bisect(simplelist, 5))

#return the leftmost value exactly equal to 8
print(bisect_left(simplelist,253))

#return on O(N)
print(simplelist.index(8))

def index_bisec(list , num):
    indx = bisect_left(list,num)
    if indx != len(list) and list[indx] == num:
        return indx
    raise Exception

#return O(log(N))
print(index_bisec(simplelist, 8))


docs = ["This is a test collection",
" This collection work on different data types",
"In each data type we will investigate the result",
"Each result probably be usable in various conditions"]

matches = [doc for doc in docs if "data" in docs]
print(matches)

set1 = {43,5543,7,3,6,33,3}
set2 = {54,32,5,3,12,65,77,3,6,88,}
#Union O(Set1 + Set2)
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
print(set3)
print(set4)
print(set5)


#Heap structure (to quickly find the maximum/minimum value in a collection)
heapq.heapify(simplelist)
heapq.heappush(simplelist,635)
print(heapq.heappop(simplelist))

#Using PriorityQueue from heapq lib
queue = PriorityQueue()
for element in simplelist:
    queue.put(element)
print(queue.get())


#Caching in Python
from functools import lru_cache
@lru_cache()
def sum(a,b):
    print("Calculating the result....")
    return a+b
#Do not use cache
print (sum(1,2))

#use cache
print(sum(1,2))

#Do not use cache
print(sum(3,4))

#Again use cache
print(sum(1,2))

print(sum.cache_info())

#Using external cache 
from joblib import Memory
mem = Memory(cachedir="/")
@mem.cache
def sum2(a,b):
    return a+b

print(sum2(4,3))