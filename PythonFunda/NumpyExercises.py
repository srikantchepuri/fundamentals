import pandas as pd
import numpy as np 

a1 = np.array([1, 2, 3, 4, 5]) 
print(a1)
print(a1.ndim)
print(a1.dtype)


a2=np.arange(1,12,2)
print(a2) #[ 1  3  5  7  9 11] , ints from 1 to 12 with step 2

a3=np.linspace(1,12,6)
print(a3) #[ 1.   3.2  5.4  7.6  9.8 12. ], floats evenely spaced 

a3=a3.reshape(3,2)
print(a3)

"""
array reshaped into 3,2 array
[[ 1.   3.2]
 [ 5.4  7.6]
 [ 9.8 12. ]]

"""
a3.dtype #dtype('float64')
a3.itemsize #8 bytes, how much each element takes up

a3.ndim # 2 dimentional

np.count_nonzero(a3) #number of non zero elements , 6

print(a3<4)

"""
[[ True  True]
 [False False]
 [False False]]

"""

a4=a3*2
print(a4)
"""
[[ 2.   6.4]
 [10.8 15.2]
 [19.6 24. ]]
"""

a5=np.zeros((3,2))
print(a5)

"""
[[0. 0.]
 [0. 0.]
 [0. 0.]]

"""


a6=np.ones((3,2))
print(a6)

"""
[[1. 1.]
 [1. 1.]
 [1. 1.]]
"""

a6=np.ones(10)
print(a6) #[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

#to get the array of random numbers from 0 to 1
a=np.random.random((3,2))
print(a)
"""
[[0.22015772 0.70486602]
 [0.53423902 0.85607235]
 [0.0645306  0.53533733]]
"""

np.set_printoptions(precision=2,suppress=None)

print(a)

"""
after precision set to 2
[0.22 0.7 ]
 [0.53 0.86]
 [0.06 0.54]]
 """
#to get the random integers as opposed to random number from 0 to 1
a=np.random.randint(0,10,11)
print(a) #[7 1 4 1 1 8 0 0 9 6 5] prints 11 random integers from 0 to 10

print(a.sum()) # 42, sum of all the numbers in a

print(a.min()) #0

print(a.max()) #9

print(a.var()) #10.330578512396695

print(a.std()) #3.214121732666125

#create a random array of 6 random integers ranging from 0 to 10 
a=np.random.randint(1,10,6)
print(a)
a=a.reshape(3,2)
print(a)
"""

[[4 5]
 [9 2]
 [3 9]]

"""

a.sum(axis=1) # sum of axis 1, sum of rows i.e [ 9 11 12]

a.sum(axis=0) #sum of axis 0, sum of columns, i.e [16, 16]









a.argmin()		# index of min element
a.argmax()		# index of max element
a.argsort()		# returns array of indices that would put the array in sorted order
a.sort()		# in place sort

# indexing, slicing, iterating
a = np.arange(10)**2
a[2]
a[2:5]

for i in a:
	print (i ** 2)
a[::-1]		# reverses array

for i in a.flat:
	print (i)

	
a.transpose()

a.ravel()			# flattens to 1D

# read in csv data file
data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1 )

print(data)

"""
[[9 3 8 7 6 1 0 4 2 5]
 [1 7 4 9 2 6 8 3 5 0]
 [4 8 3 9 5 7 2 6 0 1]
 [1 7 4 2 5 9 6 8 0 3]
 [0 7 5 2 8 6 3 4 1 9]
 [5 9 1 4 7 0 3 6 8 2]]

"""

# loadtxt does not handle missing values. to handle such exceptions use genfromtxt instead.

data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1, usecols=[0,1,2,3]) #using only first 4 cols

"""

[[9 3 8 7]
 [1 7 4 9]
 [4 8 3 9]
 [1 7 4 2]
 [0 7 5 2]
 [5 9 1 4]]

"""

a=np.arange(10)  
print(a) 

np.random.shuffle(a) # [2 0 4 1 3 6 5 9 8 7] , shuffled

np.random.choice(a)  # returns a random element from array a

np.random.random_integers(5,10,2)	# (low, high inclusive, size)





