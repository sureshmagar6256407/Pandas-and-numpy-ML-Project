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
arr = np.array([[1,2,3],
                [3,4,5]])
print(arr.shape)
"""


"""
arr  = np.arange(1,10,1)
print(arr.size)
#size is  use for  find how  much item in array
"""

"""'
mathematical operation on array
import  numpy as np  
arr = np.array([1,2,3,4,5])
print(arr+3)
print(arr-2)
print(arr*2)
print(arr/1)
"""

"""
agg_fuction
import numpy as np 
arr = np.arange(1,10,1)
print(arr)
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
print(np.std(arr))
"""

  
# arr  = np.array ( [[10,2,49,34] , 
#                    [49,29,50,19]])

# print(np.nansum(arr))
# print(np.nanmin(arr))
# print(np.nanmax(arr))
# print(np.nanvar(arr))
# print(np.nanstd(arr))
# print(np.nanmean(arr))


# import numpy as np 
# arr = np.array([1,2,3,4])
# print(arr[1])
# print(arr[3])

# arr1 = np.array([[10,11,12,13] , 
#                  [14,15,16,17]])
# print(np.nansum(arr1,axis=1))
# print(arr1[0,2])



# import numpy as np  
# arr1 = np.array([[10,11,12,13] , 
#                  [14,15,16,17],
#                  [39,90,40,60]])
# print(np.sum(arr1,axis= 0))#it's column sum  
# print(np.sum(arr1,axis=1)) #it's row sum  
# print(arr1[1,2])


# arr1 = np.array([[10,11,12,13] , 
#                  [14,15,16,17],
#                  [39,90,40,60]])
# arr = np.array([1,42,5,20,39,49,20,503,29])
# print(arr[[4,-2]])

# print(arr1[2,[0,2]])
# print(arr1[0,[2,3]])


# import numpy as np  
# arr = np.arange(1,20,1)
# print(arr[arr > 10])
# arr1  = np.array ([[39,492,50,38,29] , 
#                     [94,29,60,29,60] ])
# print(arr1 [arr1 > 50])



# import numpy as np  
# arr = np.array ([39,492,49,29])
# print(arr[ 1:2])
# print(arr[:3])
# print(arr[::2])
# print(arr[::-1])

# arr1  = np.array ([[1,39,294,50] , 
#                    [49,29, 50 ,29]])
# print(arr1[0 , 2:])
# print(arr1[1, 0:1])
# print(arr1[ : ,  :1])



# import numpy  as np  
# arr  = np.array([3,4,5,2])
# print(arr.reshape(2,2))


# arr1 = np.array([[1,3,4,5] , [4,5,2,6]])
# print(arr1.flatten())
# print(arr1.ravel())



# import numpy as np  
# arr = np.array ([10,30,29,40])
# print(arr)
# new =  np.insert(arr , 1,[49,39] , axis= None)
# print(new)

# arr1  = np.array ([[2,3,4,5] ,  
#                    [4,5,6,6]])
# print(arr1)
# new1  = np.insert(arr1,1,([10,15]) ,axis= 1)
# print(new1)
# ra  = new1.ravel()
# print(ra)
# res  = new1.reshape(5,2)
# print(res)


# import numpy as np  
# arr    =   np.array ([10,20,30])
# newArr  = np.append(arr,[50,50])
# print(newArr)

# ARR1  = np.array ([[39,29,49,20] ,
#                     [49,29,50,29]])
# # newarr = np.append(ARR1 ,[[3,4] ,[59,39]],axis= 1)
# newarr   = np.append(ARR1 , [[39,49,29,49] ], axis= 0)
# print(newarr)




# arr1  = np.array ([[2,3,4,5] ,  
#                    [4,5,6,6]])
# print(arr1)
# new1  = np.insert(arr1,1,([10,15,39,29]) ,axis= 0)
# print(new1)


# import numpy as np  
# arr1  = np.array([2,3,4])
# arr2  = np.array([3,5,2])
# newarr = np.concatenate((arr1,arr2))
# print(newarr)


# arr3   = np.array([[3,4,5,2] , 
#                    [4,5,2,5]])
# arr4  = np.array([[4,4,2,5] , 
#                   [5,7,8,2]])
# newarr1  =  np.concatenate ((arr3,arr4) ,axis= 0)
# print(newarr1)


# import numpy as np  
# arr = np.array ( [10,3,20,49])
# print(arr)
# newarr = np.delete(arr,1,axis=None)
# print(newarr)


# arr1 = np.array ([[39,29,50,11] ,  
#                   [44,19,58,18]])
# print(arr1)
# newarr1   = np.delete(arr1 ,2,axis=1 )
# print(newarr1)

import numpy as np  
arr1  = np.array([1,2,3])
arr2  = np.array ( [3,4,5])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2))) 


arr3 = np.array ( [[39,92] , [39,10]])
arr4  = np.array([[49,29] , [48,21]])
print(np.vstack((arr3,arr4)))
print(np.hstack((arr3,arr4)))