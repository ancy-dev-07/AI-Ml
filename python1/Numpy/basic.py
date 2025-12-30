import numpy as np

# nums = [1,2,3,4]
# print(nums)

# arr =np.array([1,2,3,4])
# arr =arr+5
# print(arr)


# arr2 =np.array([3,5,6,9,1,4])
# arr2 +=10

# print(arr2.ndim)   #number of dimension
# print(arr2.shape)  #rows, column
# print(arr2.size)   #total element
# print(arr2.dtype) #data type

# print(arr2)

# 2d array

# arr3 =np.array([[1,2,3],[5,6,7]])
# print(arr3+10)

# print(arr3.ndim)   #number of dimension
# print(arr3.shape)  #rows, column
# print(arr3.size)   #total element
# print(arr3.dtype) #data type


# arr4 =np.array([[5,10],[15,20]])
# print(arr4)
# print(arr4.ndim)   
# print(arr4.shape)  
# print(arr4.size)


# zero array

z =np.zeros(5)
# print(z)

# ones array

o =np.ones((2,3))
# print(o)


# range array

r = np.arange(1,10)
# print(r)

zero_10 =np.zeros(10)
# print(zero_10)

three_matrix =np.ones((3,3))
# print(three_matrix)

range_20 =np.arange(20,30)
# print(range_20)


# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr[0])
# print(arr[1:4])

# arr = np.array([5, 10, 15, 20, 25, 30])
# print(arr[0])
# print(arr[-1])
# print(arr[1:5])

# mathematic operations

# arr1 = np.array([10, 20, 30])
# arr2 = np.array([1, 2, 3])
# add =arr1+arr2
# sub =arr1 -arr2
# mul =arr1*2
# div =arr1/10
# print(f"addition of {arr1} + {arr2} ={add}")
# print(f"subtraction of {arr1} - {arr2} ={sub}")
# print(f"multiplication of {arr1} x 2 ={mul}")
# print(f"division of {arr1} by 2 ={arr1}")


# reshaping

# arr=np.arange(1,11)
# change_arr =arr.reshape(5,2)
# print(change_arr)


# arr =np.arange(1,13)
# change_arr =arr.reshape(3,4)
# change_arr2 =arr.reshape(4,3)
# print(change_arr)
# print(change_arr2)

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])


# print(arr[0:2])Get first two rows:
# print(arr[:, 2])  Get last column:
# print(arr[1, :])Get middle row:



# arr = np.array([
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ])
# print(arr[1][1])
# print(arr[:,-1])
# print(arr[arr>20])


# arr = np.array([10, 20, 30, 40])
# print(np.sum(arr))

# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))


# arr = np.array([5, 10, 15, 20])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))


# axis

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Column-wise Sum (axis=0)
# print(np.sum(arr2,axis=0))# [5 7 9]
# # Row-wise Sum (axis=1)
# print(np.sum(arr2, axis=1)) #[ 6 15 ]

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
# print(np.sum(arr))
# print(np.sum(arr,axis=0))
# print(np.mean(arr,axis=1))


# random float numbers

# print(np.random.rand())

# randomw 1d array

# print(np.random.rand(5))

# random 2d array

# print(np.random.rand(3,4))
# random int numbers

# print(np.random.randint(1,10))  #single random int number between 1 and 10
# print(np.random.randint(1,100,5))  #1d array of 5 random int number between 1 and 100
# print(np.random.randint(1,50,(3,4)))  #2d array of 3x4 random int number between 1 and 50
# print(np.random.randint(1,10,size=5))
# print(np.random.randint(1,10,size=(2,3)))

# setting seed (important for reproducibility)

# np.random.seed(42)
# print(np.random.rand(3,4))


# print(np.random.randint(10,50,(3,3)))


# np.random.seed(20)
# array=np.random.randint(1,101,5)
# print(np.max(array))
# print(np.mean(array))


np.random.seed(10)
# array=np.random.randint(1,101,(2,4))
# print(np.max(array))
# print(np.max(array,axis=0))
# print(np.mean(array,axis=1))

array=np.random.randint(10,101,(10,3))
print(np.max(array,axis=0))
print(np.mean(array,axis=1))
print(np.mean(array))