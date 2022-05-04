from numpy import sort


tex = "We are in different"
t = " part of the world"
print(tex + t)

#repeating output using multiple(*) operator
print(tex + t * 4)

#n = input("How many time do you like the text be repeated? ")
#print("Hello world" * int(n))

#slicing a string similar to slices in golang
print(tex[1:3].capitalize())

#Two form of defining sets
#x1 = set(<iter>)
x2 = {2,4,"reza"}

print(x2)
#Set operations
set1 = {"Start",2,4.5,"end"}
set2 = {5.5,"End","start",12}
#Union
print(set1|set2)
print(set1.union(set2))
set1.add(2)
set2.remove(12)
print(set2)
print(set1)
set1.difference_update(set2)
print(set1)

#Lists
myList = [12,44,"List item"]
print(myList)

list1 = [1,2,3,4,5,6,7,8,90,11,12,13,14,15,16]
print(list1)
list1[2:6] = [33,44,55,66]
print(list1)
del list1[4:6]
print(list1)
print(len(list1))
print(77 in list1)
list1.sort()
print(list1)

#Dictionary are similar to maps in golang
dic1 = {"1": 12,"2": 22,"3": 32,"4": 42,"5": 52}
print(dic1)
print(dic1["1"])
del dic1["1"]
print(dic1)
dic1.pop("2")
print(dic1)
print(dic1.values())
print(dic1.keys())

#Tuples
tup1 = (1,2,3,4,5,"six",7,"eight")
tup2 = tup1[3:4]
print(tup1)
print (tup2)
print (tup1 + tup2)

