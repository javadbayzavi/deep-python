#random number
from cmath import acos
from math import ceil, floor, hypot, radians
import random
from secrets import choice


print(random.random())
print(random.shuffle(["One",12,"Two",13,"Three",14]))
print(random.uniform(1.2,8.9))
print(random.randrange(1,9,3))

print(ceil(15.4))
print(floor(15.4))
print(pow(2,6))

print(acos(-90))
print(hypot(180,45))
print(radians(67))