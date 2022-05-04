#Recursive fibo


def fibo(n):
    if n <= 1:
        return n
    else :
        return (fibo(n - 1) + fibo(n - 2))

def ToDownFibo(n, memo):
    if memo[n] != null:
        return memo[n]
    if n <= 1:
        return n
    else:
        res = ToDownFibo(n-1) + ToDownFibo(n-2)
        memo[n] = res
        return res

def ButtomUpFibo(n):
    if n <= 1:
        return n
    list = [0] * (n+1)
    list[0] = 0
    list[1] = 1
    for i in range(2,n +1):
            list[i] = list[i - 1] + list[i -2]
    return list[n]

print(fibo(6))
#print(ToDownFibo(10,[0]))
print(ButtomUpFibo(8))

#lambda function
lambdafunc = (lambda xx, yy: xx + yy)(33 , 44)
print(lambdafunc)
print((lambda x , y :  x + y) (2,5))

#This handler define a lambda format function that receive an object and handler method that must be executed on it
handlerfunc = lambda number, func: number + func(number)
resy = handlerfunc(12, lambda z : z*z)
print(resy)
