import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# 0 - D Array : 
a = np.array(21)
print(a)

# 1 - D Array : 
a = np.array([51,62])
print(a)

#2 - D
a = np.array([[1,2] , [3,4]])
print(a)
print("Dimension: ",a.ndim)

#3-D  = two 2-D arrays
a = np.array([[[0,1], [2,3]], [[4,5] , [6,7]]])
print(a)
print("Dimension: ",a.ndim)

#dtype:
a = np.array([1,2,3])
print(a.dtype)

#shape and size
a = np.array([1,2])
print("Shape of a :",a.shape)

#change dimensions
arr = np.array([1,2,3,4] , ndmin = 5)
print(arr)
print("shape of array: " , arr.shape)

#reshape:- 
a = np.array([(8,9,10) , (11,12,13)])
print(a)
a = a.reshape(3,2)
print(a)

a = np.array([1,2,3,4])
print(a+1)
print(a**2)
b = np.ones(4) + 1
print(b)
b = np.zeros((3,3))+1
print(b)

#identity matrix
c = np.eye(3)
print(c)

c = np.eye(3,2)
print(c)
#diagonal
a = np.diag([10,12,30,4])
print(a)

#creates a numpy array from 0 to 9
a = np.arange(10)
print(a)
print(a[5])

#[start , stop , step]
b = np.arange(1,10,2)
print(b)

#it contains 6 evenly spaced nos. b/w 0 and 1
a = np.linspace(0,1,6)
print(a)


x = np.array([(8, 9 ,10) , (11,12,13)])
y = np.array([(1,2,3) , (69 , 691 , 692)])

print(x+y) 
print(np.add(x,y))
print(np.subtract(x,y))
print(np.sum(x))
print(np.sum(x , axis = 0)) #add columns 
print(np.sum(x , axis = 1)) # add rows