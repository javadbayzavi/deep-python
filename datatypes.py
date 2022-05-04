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
