import numpy as np
import json as j

# a = np.array([[1,2,3],[4,5,6],[1,3,9]])
# b = np.array([[1,3,3],[8,1,6],[3,4,5]])
# # i = np.eye(5,5)
# # # print(a-b)
# # # print(a+b)
# # # print(a*b)
# # # print(a/b)
# # # print(i)
# result = np.dot(a,b)
# print(result)


# a = np.arange(1,10,2)
# print(a)

# a = np.linspace(0,1,10)
# print(a)

# A = np.array([[1,2,3],
#               [6,2,8],
#               [3,6,1]])
# B = np.array([[2,4,6],
#               [9,8,1],
#               [2,3,4]])
# print("Sum of a and b: \n" , A+B)
# print(np.dot(A, B))


# a = np.array([5, 10, 15, 20])
# print(a)

# a = np.array([[1,4],[3,4]])
# b = np.array([[9,7],[5,8]])
# print(a+b)

# a = np.array([[1,4],[3,4]])
# b = np.array([[9,7],[5,8]])
# print(np.dot(a,b))

# a = np.array([[1,2,3],[2,3,4],[2,6,8]])
# print(a.T)

# a = np.array([[1,2,3],[2,3,4],[2,6,8]])
# print(a.shape)
# print(a.size)
# print(a.dtype)

# a = np.array([[1,4],[3,4]])
# b = np.array([[9,7],[5,8]])
# print(a - b)
# print(a + b)
# print(a / b)
# print(a * b)


# a = np.eye(3)
# print(a.astype(int))


# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# a_reshaped = a.reshape(3,4)
# print(a_reshaped)

# a = np.array([[2,5],
#               [3,2]])
# b = np.array([[5,6],
#               [2,4]])
# print(np.dot(a,b))


a = np.array([[10,20,30,40],
              [50,60,70,80],
              [90,100,110,120],
              [130,140,150,160]])
# print(a[0:2,1:3])
# print(a[1::2,0::3]) shows the result : [[ 50  80]
#                                         [130 160]]

# print(a[::-1])  reversing all rows
# print(a[::,::-1]) reversing the all columns


# print(a[2:4,0:4]) getting the last rows of a
# print(a[0:2,2:4]) getting the top-right 2x2 corner
# print(a[:,0::2])  getting all even-indexed columns

# print(a[1:3,1:3])
# print(a[0:3,2:4])
# print(a[::-1])
# print(a[[0,1,2,3],[2,3,3,1]]) this is a fancy indexing in this first vector is for selecting rows and the second vector is for choosing elements from the selected rows
# print(a[:,0:1]) getting the first column as column vector

# Broadcasting in numpy

# 1: Scalar broadcasting --> In this it stretch the b to perform some elements-wise operations
# a = np.array([1,2,3])
# b=10
# print(a+b)

# 2: Row + Column(2D Broadcasting)
# a = np.array([[1],
#               [2],
#               [3]])
# b = np.array([10,20,30])
# print(a+b)

# 3:1D to 2D bradcasting
# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([10,20,30])
# print(a * b)

# a = np.array([[1,2,3],
#               [3,4,3]])
# b = np.array([[2],
#               [3]]) in this it will add column wise
# # b_reshaped = b.reshape(2,2)
# # print(b_reshaped+a)
# print(a.shape)
# print(b.shape)
# print(a+b)

# a = np.array([[1,2,3],
#               [3,4,3]])
# b = np.array([2,3,3])  in this it will add row wise 
# # b_reshaped = b.reshape(2,2)
# # print(b_reshaped+a)
# print(a.shape)
# print(b.shape)
# print(a+b)

# Problems on broadcasting
# a = np.array([[1,2],
#               [3,4]])
# b = 3
# print(a*b)

# a = np.array([10,20,30])
# b = np.array([[1],
#               [2],
#               [3]])
# print(a+b)

# a = np.array([[4,2,0],
#               [8,7,6]])
# b= np.array([[2],
#              [2]])
# print(a-b)


# a = np.array([[1,2,3],
#               [4,5,6]])
# b = np.array([[2],
#               [2]])
# print(a/b)

# a = np.array([[5,10,15],
#               [10,20,30],
#               [15,30,45]])
# b = np.array([[2],
#               [2],
#               [2]])
# print(a*b)

# a = np.array([[1],
#               [2],
#               [3],
#               [4]])
# b = 10
# print(a*b)

# a = np.array([[1,2,3,4],
#               [2,4,6,8]])
# b = np.array([[2],
#               [2]])
# print(a*b)

# a = np.array([1,2,3])
# b = np.array([[1],
#               [1],
#               [1]])
# print(a*b)


# 5: Boolean Masking --> In this we use the condition as boolean instead of loops to make it faster and cleaner


# a = np.array([1,3,3,5])
# even = a[a%2==0]
# print(even)

# a = np.array([5,10,15,20,25])
# mask = a > 15
# print(a[mask])

# a = np.array([1,2,3,4,5,6])
# even = (a%2 == 0)
# print(a[even])

# a = np.array([3,6,9,12])
# mask = (a > 5) & (a<12)
# print(a[mask])

# a = np.array([10, 20, 30, 40, 50])
# mask = (a==10) | (a==50)
# print(a[mask])

# a = np.array([2, 4, 6, 8, 10])
# a[a>6] = 99
# print(a)

# a = np.array([1, 0, -1, -5, 3])
# mask = a<0
# print(a[mask])

# a = np.array([5, 10, 15, 20])
# mask = (a%10==0)
# print(mask)

# a = np.array([10, 15, 20, 25, 30])
# print(a[1:4][a[1:4] > 18])
# This is a concept of Slicing + Masking 

# 6: Conditional Updates

# a = np.array([1,-2,0,4,-5])
# a[a<0] = a[a<0] * (-1)
# print(a)

# a = np.array([30, 55, 70, 40, 90])
# a[a<50] = 0
# print(a)

# a = np.array([5, 10, 15, 3, 0])
# a[a<10] = 0
# a[a>=10] = 1 
# print(a)

# a = np.array([3, 6, 7, 8, 9, 10])
# a[a % 3 != 0] = -1
# print(a)

# a = np.array([5, 10, 20, 30, 40])
# a[(a>=10) & (a<40)] = a[(a>=10) & (a<40)] * 2
# print(a)

# a = np.array([2, 5, 12, 14, 9, 17])
# mask = (a%2==0) & (a>10)
# a[mask] = 100
# print(a)

# 7: Vectorized Operations

# a = np.array([1,2,3])
# b = np.array([3,4,5])
# res = a**b
# print(res)



# a = np.array([1, 2, 3, 4, 5])
# print(a+5)

# a = np.array([2, 4, 6])
# print(a*3)

# a = np.array([1, 3, 5])
# print(a**2)

# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# print(a-b)

# a = np.array([8, 10, 12])
# f_arr = a/2
# print(f_arr)


# Advanced topic 1 - np.where() and np.select()
# np.where() - it is used as if else but in one line instruction and in vectorized
# np.select() - it is for multiple conditions like if-elif-else 

# marks = np.array([35, 60, 45, 20, 85])
# result = np.where(marks >= 40,"Pass","Fail")
# print(result)

# nums = np.array([1,2,3,4,5,6])
# mask = (nums %2==0)
# value = nums[mask]=0
# result = np.where(mask,value,1)
# print(result)

# scores = np.array([95,88,72,60,40])
# conditions = [scores>=90,scores>=70]
# value = ("A","B")
# result = np.select(conditions,value,"C")
# print(result)

# temps = np.array([10,18,25,35,5])
# conditions = [temps>=30,temps>=15,temps<15]
# value = ("Hot","Warm","Cold")
# result = np.select(conditions,value,"")
# print(result)

# a = np.array([5,-2,9,-4,0])
# mask = a<0
# result = np.where(mask,0,a)
# print(result)

# Advanced Topic 2 - Aggregation functions
# sum(),mean(),max(),min(),std(),var()

# a = np.array([1, 2, 3, 4, 5])
# std = np.std(a)
# var = np.var(a)
# print("std:" , std)
# print("var:" , var)

# b = np.array([5, 5, 5, 5])
# std = np.std(b)
# var = np.var(b)
# print("std:" , std)
# print("var:" , var)

# c = np.array([10, 50, 90])
# std1 = np.std(c)
# var1 = np.var(c)
# conditions = [std1<std and var1<var,std1>std and var1>var]
# values = ("std1: Less than Problem 1\n var1: Less than Problem 1","std1: Higher than Problem 1\nvar1: Much higher than Problem 1")
# result = np.select(conditions,values,"")
# print(result)

# d = np.array([[1, 2, 3],
#               [4, 5, 6]])
# std = []
# std = np.std(d,axis=0)
# std1 = []
# std1 = np.std(d,axis=1)
# print("axis=0 std:", std)
# print("axis=1 std:", std1)

# e = np.array([-3, 0, 3])
# std = np.std(e)
# var = np.var(e)
# print("std:", std)
# print("var:", var)

# a = np.array([10, 20, 30, 40, 50])
# sum = np.sum(a)
# mean = np.mean(a)
# var = np.var(a)
# std = np.std(a)
# print("sum: ",sum)
# print("mean: ",mean)
# print("std: ",std)
# print("var: ",var)

# b = np.array([7, 3, 9, 5])
# print("min: ",np.min(b))
# print("max: ",np.max(b))
# print("argmin: ",np.argmin(b))
# print("argmax: ",np.argmax(b))

# c = np.array([2, 4, 6])
# print("cumsum: ",np.cumsum(c))
# print("prod: ",np.prod(c))

# d = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print("sum(axis=0): ",np.sum(d,axis=0))
# print("max(axis=1): ",np.max(d,axis=1))

# e = np.array([10, 20, 30, 40, 50])
# print("25th: ",np.percentile(e,25))
# print("50th: ",np.percentile(e,50))
# print("75th: ",np.percentile(e,75))


# 3: Advanced Topic - Fancy Indexing 
# np.ix_() - it is used to getting a submatrix


# a = np.array([[1,2,3],
#               [2,3,4],
#               [3,4,5]])
# rows = [1,2]
# cols = [1,2]
# print(a[np.ix_(rows,cols)])

# a = np.array([[1,2,3],
#               [2,3,4],
#               [3,4,5]])
# rows = [0,2]
# cols = [2,0]
# print(a[np.ix_(rows,cols)])

# 4: Advanced Topics - Views and Copies

# a = np.array([100,200,300,400])
# b = a[2:]
# b[0] = 999
# print(b)

# a = np.array([1,2,3,4])
# b = a[[1,3]]
# b[1] = 999
# print(a)
# print(b)

# 5: Advanced Topic - Structured Array

# students = np.array([(101,"kamal",95.0),
#                      (102,"vikas",90)],
#                      dtype = [("id","i4"),("name","U10"),("marks","f4")])
# print(students[0])
# print(students.dtype)



# 6: Advanced Topic - Linear Alegbra with np.linalg

# a = np.array([[1, 2],
#               [3, 4]])
# b = np.array([[5, 6],
#               [7, 8]])

# result = a @ b
# print(result) it is basically a dot product


# A = np.array([[2, 1],
#               [1, 3]])

# vals, vecs = np.linalg.eig(A)

# print("Eigenvalues:", vals)
# print("Eigenvectors:\n", vecs)


# a = np.array([[1, 2, 3],
#               [0, 1, 4],
#               [5, 6, 0]])
# print(round(np.linalg.det(a)))

# 7: Advanced Topic - np.random()

# nums = np.random.randint(0,10,1)
# print(nums) it will print the random integers

# nums = np.random.randint(0,10,size = (3,3))
# print(nums) it will print the  matrix with random elements

# nums = np.random.rand(3,2)
# print(nums) 


# nums = np.random.randn(3,2)
# print(nums)

# print(np.random.seed(40))
# # print(nums)

# np.random.seed(42)
# print(np.random.randint(1, 10, size=3))


# arr = np.array([1,2,3,4])
# np.random.shuffle(arr)
# print(arr) shuffles the array

# arr = np.random.choice([10, 20, 30, 40], size=3)
# print(arr)

# practice problems

# list comprehension
# numbers = [1,2,3,4,5]
# squares = [i**2 for i in numbers]
# print(squares)

# lambda function
# cube = lambda x:x**3
# print(cube(2))

# file
# wi

# practice problems
# colors = ["red","blue","yellow","black"]
# for index,color in enumerate(colors):
#     print(index,color)

# players = ["Dhoni","Virat"]
# roles = ["WicketBatsmen","Batsmen"]
# for p,r in zip(players,roles):
#     print(f"{p} is a {r}")


# try:
#     result = 10/0
# except ZeroDivisionError:
#     print(ZeroDivisionError)

# nums = [1,2,3]
# cube = list(map(lambda x: x**2,nums))
# print(cube)

# Courses = ["DataScience","python","Ml","Btech"]
# filter = list(filter(lambda word : len(word)>2,Courses))
# print(filter)