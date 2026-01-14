import numpy as np

arr = np.array([1, 2, 3, 4, 5, 7, 8, 1, 3, 5, 3, 4, 6, 8, 9, 1, 2, 4, 6, 8])
uniques, counts = np.unique(arr, return_counts=True)
print(uniques)
print(counts)

# intersection, differentiation, neither
arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([5, 7, 9, 11])

print(np.intersect1d(arr1, arr2)) # Elements present in both
print(np.union1d(arr1, arr2))     # All unique elements from both
print(np.setdiff1d(arr1, arr2))   # Elements in arr1 but not in arr2
print(np.setxor1d(arr1, arr2))    # Elements in either arr1 or arr2, but not both