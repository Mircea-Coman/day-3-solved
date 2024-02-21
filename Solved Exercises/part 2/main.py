import numpy as np

# a) Create a null vector of size 10 but the fifth value which is 1
v_a = np.zeros([10])
v_a[4] = 1
print(f"a) {np.array2string(v_a)}\n")

#b) Create a vector with values ranging from 10 to 49
v_b = np.arange(10, 50)
print(f"b) {np.array2string(v_b)}\n")

#c) Reverse a vector (first element becomes last)
v_original_c = np.random.rand(5)
v_reversed_c = v_original_c.copy()[::-1]
print(f"c) Original vector: {np.array2string(v_original_c)}")
print(f"    Flipped vector: {np.array2string(v_reversed_c)}")

#d) Create a 3x3 matrix with values ranging from 0 to 8
m_d = np.arange(9).reshape(3, 3)
print(f"d) \n {np.array2string(m_d)}\n")

#e) Find indices of non-zero elements from [1,2,0,0,4,0]
v_e = np.array([1,2,0,0,4,0])
indices = np.where(v_e != 0)
print(f"e) Indices of non-zero elements: {np.array2string(indices[0])}\n")

#f) Create a random vector of size 30 and find the mean value
v_f = np.random.rand(30)
mean = np.mean(v_f)
print(f"f) Mean of a size {v_f.size:d} vector is {mean:f}\n")

#g)  Create a 2d array with 1 on the border and 0 inside
n_x = 5
n_y = 4
array_g = np.zeros([n_x, n_y], dtype=np.byte)
array_g[0, :] = array_g[-1, :] = array_g[:, 0] = array_g[:, -1] = 1
print(f"g) \n{np.array2string(array_g)}\n")

#h) Create a 8x8 matrix and fill it with a checkerboard pattern
array_h = np.zeros([8, 8], dtype = np.byte)
array_h[::2, ::2] = array_h[1::2, 1::2] = 1
print(f"h) \n{np.array2string(array_h)}\n")

#i) Create a checkerboard 8x8 matrix using the tile function
array_i = np.tile(np.array([[1, 0], [0, 1]]), [4, 4])
print(f"i) \n{np.array2string(array_i)}\n")

#j) Given a 1D array, negate all elements which are between 3 and 8, in place
v_j = np.arange(11)
mask = np.logical_and(v_j>=3, v_j<= 8)
v_j[mask] = -v_j[mask]
print(f"j) {np.array2string(v_j)}\n")

#k) Create a random vector of size 10 and sort it
v_k = np.random.random(10)
v_k_sorted = np.sort(v_k)
print(f"k) Original Array: {np.array2string(v_k)}")
print(f"     Sorted Array: {np.array2string(v_k_sorted)}\n")

#l) Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = (A==B).all()
print(f"l) A = {np.array2string(A)}")
print(f"   B = {np.array2string(B)}")
if equal:
    print("The arrays are equal :) \n")
else:
    print("The arrays are NOT equal :( \n")

#m) How to convert an integer (32 bits) array into a float (32 bits) in place?
v_m = np.arange(10, dtype=np.int32)
print(f"m) Original dtype: {v_m.dtype}")
v_m = v_m.astype(np.float32)
print(f" New dtype: {v_m.dtype}\n")

#n) How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(f"n) A.B = \n{np.array2string(C)}")
print(f"diagonal = {np.array2string(D)}")
