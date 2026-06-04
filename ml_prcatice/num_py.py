import numpy as np

#creation
"""
# one dimensional array
numpy_array  = np.array([1,2,3,4])
print(numpy_array)
"""


"""
# two dimensional array
arr_2d = np.array([[1,2,3],
                   [4,5,6]])
print(arr_2d)
"""

"""
# three dimensional array
multi_dimensional  = np.array([[[1,2,3],
                                [4,5,6]]])
print(multi_dimensional)
"""


""""
#with deafault value where all value are 0
zeros_array  = np.zeros([3,4])
zeros  = np.zeros(4)
print(zeros)
print()
print(zeros_array)
"""


"""
#ones  
ones_array = np.ones((3,4))
one  = np.ones(3)
print(one)
print()
print(ones_array)
"""


"""
#full array  you need to pass shape and which value do you want to fill there
fill_array = np.full((2,3),6)
print(fill_array)
"""


"""
#arange  is like the loop but it's python numpy loop
arr  = np.arange(1,11,2) 
print(arr)
"""

""" 
#creating identity matices 
#eye(size) first when we give size its make the 1 center and all side 0
identity  = np.eye(3)  
print(identity)
"""


#array attributes
"""
#astype  - astype is use to change the number  onto the flot interger as it data type
arr  = np.array([2,3,4,5,6])
int_arr  = arr.astype(float)
print(arr)
print(int_arr)
"""


"""
#dtype   - dtype use for data type of variable
ar = np.arange(1,10,1)
print(ar)
print(ar.dtype)
"""

"""
ndim  - uses for find the dimmensiona of array
arr1  = np.full((1,2),4)
arr2= np.zeros(3)
print(arr1)
print(arr2)
print(arr1.ndim)
print(arr2.ndim)
"""

"""
#shape is use for row and column 
"""
arr = np.array([[1,2,3],
                [3,4,5]])
print(arr.shape)