import numpy as np

# Create a 1D array of numbers from 1-5
A = np.array([1, 2, 3, 4, 5]) 
print("Original array A:")
print(A)

# Print first element (index 0)
print("First element of array A:")
print(A[0])

# Print fourth element (index 3)
print("Fourth element of array A:")
print(A[3])

# Print type of variable holding array A
print("Type of array A:")
print(type(A))

# Print shape of the array (1 row, 5 columns)
print("Shape of array A:")
print(A.shape)

# Modify first element to 10
print("Changing first element of array A to 10:")
A[0] = 10
print(A)

A = np.append(A, 6)  # Append 6 to the end of array A
print("Array A after appending 6:")
print(A)

A = np.insert(A, 2, 15)  # Insert 15 at index 2
print("Array A after inserting 15 at index 2:") 
print(A)

A = np.delete(A, 4)  # Delete element at index 4
print("Array A after deleting element at index 4:")
print(A)

C = np.array([7, 8, 9])  # Create another array C
A = np.concatenate((A, C))  # Concatenate array C to array A 
print("Array A after concatenating [7, 8, 9]:")
print(A)

D = np.copy(A)  # Create a copy of array A into D
print("Array D as a copy of array A:")
print(D)

# Create a 2D array with two rows and two columns
B = np.array([[1, 2], 
              [3, 4]])
print("New array B with two dimensions:")
print(B)

# Print element at second row, first column (index 1,0)
print("Element at position [1,0] in array B:")
print(B[1,0])

# Create array of zeros with shape defined by a list
print("Array of zeros with shape defined by a list [[1,2],[3,4]]:")
print(np.zeros((2,3)))

# Repeat elements of an array
arr = ['Harish', 1, 2]
print(np.repeat(arr,3))

# Generate and work with B as before

# Create a new 6x6 random array
B = np.random.rand(6,6)
print("Random 6x6 array B:")
print(B)

# Extract the diagonal elements of B
diag_B = np.diag(B)
print("Diagonal elements of B:")
print(diag_B)

# Get properties of array B
print(f"Array B has {np.ndim(B)} dimensions")
print(f"It has a shape of {np.shape(B)}")
print(f"It contains {np.size(B)} elements")

# Create an array with random values
E = np.random.rand(2,2)
print("Array E with random values between 0 and 1:")
print(E)

# Repeat elements in a new example array
repeat_arr = np.array([1, 2, 3])
repeated_arr = np.repeat(repeat_arr, 3)
print("Repeating elements of the array [1, 2, 3] three times:")
print(repeated_arr)

B/2  # Element-wise division of B by 2
print("Half of B elements:")
print(B/2)

np.exp(B)  # Element-wise exponential of B
print("Exponential of B elements:")
print(np.exp(B))

# Logmarithm base 2 of B elements
np.log2(B)
print("Log base 2 of B elements:")
print(np.log2(B))   

# Element-wise tangent of B
np.tan(B) 
print("Tangent of B elements:")
print(np.tan(B))

np.sum(B)  # Sum of all elements in B
print("Sum of all elements in B:")
print(np.sum(B))

np.min(B)  # Minimum element in B
print("Minimum element in B:")  
print(np.min(B))

np.sum(B, axis=0)  # Sum of each column in B
print("Sum of each column in B:")   
print(np.sum(B, axis=0))

np.sum(B, axis=1) # Sum of each row in B
print("Sum of each row in B:")
print(np.sum(B, axis=1))

np.min(B, axis=0)  # Minimum of each column in B
print("Minimum of each column in B:")
print(np.min(B, axis=0))

np.max(B, axis=1)  # Minimum of each row in B
print("Maximum of each row in B:")
print(np.max(B, axis=1))

np.median(B, axis=1)  # Median of each row in B
print("Median of each row in B:")
print(np.median(B, axis=1))

np.std(B)  # Standard deviation of all elements in B
print("Standard deviation of all elements in B:")
print(np.std(B))

np.var(B)  # Variance of all elements in B
print("Variance of all elements in B:")
print(np.var(B))

np.sort(B, axis=0)  # Sort each column of B
print("Sorted elements of B:")
print(np.sort(B, axis=0))

# Transpose of B
print("Transpose of B:")
print(B.T)

B.flatten()  # Flatten B to 1D array
print("Flattened array B:")
print(B.flatten())

