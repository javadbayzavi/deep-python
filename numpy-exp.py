import numpy as np

np_array = np.array([1,2,3,4,5,6,7,8], dtype="float32")
np_array.astype("float32")
print(np_array.dtype)

np_rr = np.array([["a","b","c"],[1,2,3]])
#Return the shape of the array and in this case it contains 2rows(samples) and 3columns(features)
print(np_rr.shape)

#example of reshaping arrays 
np_resharr = np.array([[1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1]])
print(np_resharr.shape)

#reshape the orignal 2,9 array to 3,6. Note for reshaping, the number of element in each reshaping
#must not changed
reshaped = np_resharr.reshape(3,6)
print(reshaped.shape)

#full zero array
zer_arr = np.zeros((4,4))
print(zer_arr)

#full one array
one_arr = np.ones((4,4), dtype="int32")
print(one_arr)

#empty arr
empt_arr = np.empty((3,3) , dtype="bool")
print(empt_arr)

#Random value array
rnd_arr = np.random.rand(3,3)
rnd_arr.astype("int32")
print(rnd_arr)

#full zero array similar to input array. Note: similar function for ones_like and empty_like
zlink_arr = np.zeros_like(empt_arr)
print(zlink_arr)

#accessing array elements
print("Element of zlike array:", [a for a in zlink_arr])

#using array as index for another array
mainarr = np.array([[9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9],[10,2,30,40,50,60,70,80,80]])
indexrr = np.array([[0,1,2],[2,1,0],[1,2,0]])
print(mainarr[indexrr])

#sample of swaping array columns using slices
r = np.random.rand(8,2)
print(r)
r[:,[0,1]] = r[:,[1,0]]
print(r)

#indexing using take and compress functions
r_i = np.random.rand(100,2)
idx = np.arange(50)
yx = np.take(r_i,idx,axis=0)

print(yx)

#calculating the norm for a vector
r_ = np.random.rand(10,2)
norm = np.sqrt((r_ ** 2).sum(axis=1))
print(r_.sum())
print(norm)