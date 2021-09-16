import numpy as np


arr1 = list(range(1000))
arr2 = list(range(1000,2000))

#pure python
result1 = 0
for x1, x2 in zip(arr1,arr2):
    result1 += x1*x2
print(result1)

#use numpy
result2 = np.dot(arr1,arr2)
print(result2)

#array 3D
arr = np.array([
    [
        [1,2,3,4],
        [1,2,3,4]
    ],

    [
        [1,2,3,4],
        [1,2,3,4]
    ]
])
print(arr.shape)
