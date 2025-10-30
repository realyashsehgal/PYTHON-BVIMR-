from Signature_folder.Signature import sign

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

add = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

sub = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

mul = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

transpose_A = [[A[j][i] for j in range(3)] for i in range(3)]

print("Matrix A:", A)
print("Matrix B:", B)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Transpose of A:", transpose_A)

sign()
