"""Create a `Matrix` class to represent a 2D matrix. 
    Add methods for matrix addition, subtraction, and multiplication."""

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix.")

        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return Matrix(result)


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


C = A + B
print("\nMatrix A + B:")
print(C)


D = A - B
print("\nMatrix A - B:")
print(D)


E = A * B
print("\nMatrix A * B:")
print(E)


F = A.transpose()
print("\nTranspose of A:")
print(F)

G= F.transpose()
print(G)