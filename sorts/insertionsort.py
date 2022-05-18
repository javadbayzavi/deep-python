import time


def insertion_sort(InputList):
   for i in range(1, len(InputList)):
    j = i-1
    nxt_element = InputList[i]
    while (InputList[j] > nxt_element) and (j >= 0):
        InputList[j+1] = InputList[j]
        j=j-1
    InputList[j+1] = nxt_element

lst = [22,54,8,12,9,56,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,1,45,267,3,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,6,2,5,7,39,7,4,7,39,7,4,22,54,8,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4]
start = time.time()
insertion_sort(lst)
end = time.time()
print(lst)
print(end - start)