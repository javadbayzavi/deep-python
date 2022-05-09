import numba as nb

def sum_a(a):
    res = 0
    n = len(a)
    for i in range(n):
        res += a[i]
    return res
print(sum_a([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,0]))

@nb.jit
def sum_ajit(a):
    res = 0
    n = len(a)
    for i in range(n):
        res += a[i]
    return res

print(sum_ajit([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,0]))