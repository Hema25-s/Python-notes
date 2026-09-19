#                       NUMPY
'''
Numerical python is the module used to do math operations on 
large dim array or list

Compare to normal array numpy array math caculations are performs
math operation on multi dim numerical data.

This module needs to be installed using following command

pip install numpy - run this on ternimal

             WHAT IS PIP

Python module install manager, it is used to install new python files
or folder from online.


              WHAT IS NUMPY ARRAY

A function used to create multi dim array

EX:


import numpy as np

a = np.array([1,2,3,4,5]) # 1D array

b = np.array([
    [1,2,3],
    [4,5,6]
]) # 2D array

c = np.array([
    [
        [1,2,3],
        [4,5,6]
    ]
]) # 3D array

print(a+1)
print(b+1)
print(c+1)



'''

#            BOARDCASTING
'''


Performing math operations between two different dim array
For that both array should have same no of columns


import numpy as np

a = np.array([1,2,3,4,5]) # 1D array

b = np.array([
    [1,2,3],
    [4,5,6]
]) # 2D array

c = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
            [1,2,3],
            [4,5,6]
        ],
]) # 3D array



print('a: ',a.shape) # gives no of row and columns
print('b: ',b.shape) # (2-row, 3-col)


print('a: ',a.shape) # gives no of row and columns
print('b: ',b.shape)
print('b: ',b.shape[1])
print('c: ',c.shape)


EX2:



import numpy as np

a = np.array([1,2,3]) # 1D array

b = np.array([
    [1,2,3],
    [4,5,6]
]) # 2D array

c = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
            [1,2,3],
            [4,5,6]
        ],
]) # 3D array


print(b+c)

'''


#         INDEXING AND SLICING
'''


import numpy as np

a = np.array([1,2,3]) # 1D array

b = np.array([
    [1,2,3],
    [4,5,6]
]) # 2D array

c = np.array([
    [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12]
    ]
]) # 3D array

print(a[2]) # 1D
print(b[0][-1]) # 2D
print(c[0][1][-1]) # 3D

print(c[0][1][1:4])


c[0][1][-1] = 24
print(c)

c[0][1][1:4] = 10
print(c)

c[0][1][1:4] = [10,20,30]
print(c)

'''

#                    MATH FUNCTIONS
'''
import numpy as np

a = np.array([1,2,3]) # 1D array

b = np.array([
    [1,2,3],
    [4,5,6]
]) # 2D array

print(b.sum())
print(b.sum(axis=0)) # col wise sum
print(b.sum(axis=1)) # row wise sum

print(b.mean(), b.min(), b.max(), b.sort(), b.astype(dtype='float'), b.dtype)
print(b.cumsum()) # adds current and previous value
print(b.cumprod())

c= np.array([
    [1,2],
    [4,5],
    [7,8]
])
print(c.diagonal().sum())


print(c.reshape(2,3))
print(c.reshape(1,-1))


'''

#            RANDOM ARRAY

'''

import numpy as np 
a = np.random.rand(3,3)

a = np.random.randn(3,3)
a = np.random.randint(10,20,(3,3))

a=np.linspace(start=10, stop=11, retstep=True, num=10)

a=np.zeros(shape=(2,2))
a=np.ones(shape=(2,2))

b = np.array([
    [1,2,3],
    [4,5,6]
])

a=np.zeros_like(b)
print(a)



            WHERE

import numpy as np

b = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.where(b>4,b,0))
'''
