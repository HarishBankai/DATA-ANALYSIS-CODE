import numpy as np
# Create a 1D array of numbers from 1-5
A = np.array([1, 2, 3, 4, 5]) 
print("Original array A:")
print(A)  # Prints the array and its elements

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
print(A)  # Shows updated array

# Create a 2D array with two rows and two columns
B = np.array([[1, 2], 
          [3, 4]])
print("New array B with two dimensions:")
print(B)

# Print element at second row, first column (index 1,0)
print("Element at position [1,0] in array B:")
print(B[1,0])

# Print shape of array B (2 rows, 2 columns)
print("Shape of array B:")
print(B.shape)

C = np.arange(1,10,2)  # Create array from 1 to 10 with step of 2
print("Array C with values from 1 to 10 with step 2")
print(C)

D = np.linspace(0,10,40)  # Create array of 40 values evenly spaced between 0 and 10
print("Array D with 40 values evenly spaced between 0 and 10")
print(D)

E = np.random.rand(2,2) #Create (2,2) aray of random numbers between 0 and 1
print("Array E with random values between 0 and 1:")
print(E)

np.zeros((3,3)) #Create (3,3) array of zeros
print("Array of zeros with shape (3,3):")       
print(np.zeros((3,3)))

np.ones((2,3)) #Create (2,3) array of ones
print("Array of ones with shape (2,3):")        
print(np.ones((2,3)))

# Create array of zeros with shape defined by a list
print("Array of zeros with shape defined by a list [[1,2],[3,4]]:")   
print(np.zeros((2,3)))

# Repeat elements of an array
arr = ['Harish', 1, 2]
print(np.repeat(arr,3))