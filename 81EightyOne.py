from Signature_folder.Signature import sign
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

add = A + B
sub = A - B
mul = np.dot(A, B)
transpose_A = A.T

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Addition:\n", add)
print("Subtraction:\n", sub)
print("Multiplication:\n", mul)
print("Transpose of A:\n", transpose_A)

sign()
