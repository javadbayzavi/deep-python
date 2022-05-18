import time


def linearsearh(lst , element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

lst = [22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4]


start = time.time()

res = linearsearh(lst, 12)
end = time.time()
print(res)
print('result has found in :' + str(end - start))
