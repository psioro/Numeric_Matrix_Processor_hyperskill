import copy
from math import pow

def get_matrix_NEW(ident=""):
    dim = [int(x) for x in input(f"Enter size of {ident} matrix: ").split()]
    print(f"Enter {ident} matrix")
    matrix = []
    for _ in range(dim[0]):
        matrix.append([float(x) for x in input().split()])
    return matrix

def get_matrix(dim):
    matrix = []
    for _ in range(dim):
        matrix.append([float(x) for x in input().split()])
    return matrix


def print_matrix(mx):
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            print(mx[i][j], end=" ")
        print()


def add_matrix(mx1, mx2):
    row = len(mx1)
    column = len(mx1[0])
    result = []
    for i in range(row):
        sum_temp = []
        for j in range(column):
            sum_temp.append(mx1[i][j] + mx2[i][j])
        result.append(sum_temp)
    return result


def multiply_matrix_by_constant(matrix, const):
    row = len(matrix)
    column = len(matrix[0])
    result = []
    for i in range(row):
        multiply_temp = []
        for j in range(column):
            multiply_temp.append(matrix[i][j] * const)
        result.append(multiply_temp)
    return result


def zero_matrix(rows, cols):
    # Creates matrix full of zeros with given rows and columns
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0)
    return M


def multiply_matrices_new(mx1, mx2):
    if len(mx1[0]) == len(mx2):
        result = zero_matrix(len(mx1), len(mx2[0]))
        for i in range(len(mx1)):
            for j in range(len(mx2[0])):
                for k in range(len(mx2)):
                    result[i][j] += mx1[i][k] * mx2[k][j]
        return result
    else:
        print("The operation cannot be performed.")


def transpose_diag_main(matrix):
    result = zero_matrix(len(matrix), len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[j][i]
    return result


def transpose_vertical(matrix):
    result = zero_matrix(len(matrix), len(matrix[0]))
    for i in range(len(matrix)):
        result[i] = matrix[i][::-1]
    return result


def transpose_horizontal(matrix):
    result = matrix[::-1]
    return result


def reduced(mx_to_reduce, row, column):
    minor_mx = copy.deepcopy(mx_to_reduce)
    for i in range(len(mx_to_reduce)):
        del(minor_mx[i][column])
    del(minor_mx[row])
    return minor_mx


def determinant(mx):
    size = len(mx)
    if size == 1:
        return mx[0][0]
    elif size == 2:
        return mx[0][0] * mx[1][1] - mx[0][1] * mx[1][0]
    else:
        result = 0
        for i in range(len(mx)):
            # result = matrix element[first row, i-th element] * cofactor * minor[0,i]
            result += mx[0][i] * pow(-1, (1 + i+1)) * determinant(reduced(mx, 0, i))
        return result


def inverse(mx):
    det = determinant(mx)
    if det == 0:
        return print("This matrix doesn't have an inverse.")
    else:
        mx_cofactors = zero_matrix(len(mx), len(mx))
        for i in range(len(mx)):
            for j in range(len(mx)):
                mx_cofactors[i][j] = pow(-1, (i+1 + j+1)) * determinant(reduced(mx, i, j))
        mx_cofactors_T = transpose_diag_main(mx_cofactors)
        result = multiply_matrix_by_constant(mx_cofactors_T, (1 / det))
        return result


# =============================================


while True:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices"
          "4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    command = int(input("Your choice: "))
    if command == 0:
        break
    elif command == 1:
        # add matrices
        #dim1 = [int(x) for x in input("Enter size of first matrix: ").split()]
        #print("Enter first matrix: ")
        #matrix1 = get_matrix(dim1[0])
        matrix1 = get_matrix_NEW("first")
        matrix2 = get_matrix_NEW("second")

        #dim2 = [int(x) for x in input("Enter size of second matrix: ").split()]
        #print("Enter second matrix: ")
        #matrix2 = get_matrix(dim2[0])
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            print("The result is: ")
            print_matrix(add_matrix(matrix1, matrix2))
        else:
            print("The operation cannot be performed.\n")
        del (matrix1, matrix2)
        #del (dim1, dim2, matrix1, matrix2)
    elif command == 2:
        # multiply matrices by constant
        dim1 = [int(x) for x in input("Enter size of the matrix: ").split()]
        print("Enter matrix:")
        matrix1 = get_matrix(dim1[0])
        constant = float(input("Enter constant: "))
        print("The result is:")
        print_matrix(multiply_matrix_by_constant(matrix1, constant))
        del (dim1, matrix1, constant)
    elif command == 3:
        # multiply matrices
        dim1 = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        matrix1 = get_matrix(dim1[0])
        dim2 = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter second matrix: ")
        matrix2 = get_matrix(dim2[0])
        print("The result is: ")
        print_matrix(multiply_matrices_new(matrix1, matrix2))
        del (dim1, dim2, matrix1, matrix2)
    elif command == 4:
        # transpose matrices
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        command_transpose = int(input("Your choice: "))
        if command_transpose == 1:
            # Transpose along main diagonal
            dim1 = [int(x) for x in input("Enter matrix size: ").split()]
            print("Enter matrix:")
            matrix1 = get_matrix(dim1[0])
            print("The result is:")
            print_matrix(transpose_diag_main(matrix1))
            del (dim1, matrix1)
        elif command_transpose == 2:
            # Transpose along side diagonal
            dim1 = [int(x) for x in input("Enter matrix size: ").split()]
            print("Enter matrix:")
            matrix1 = get_matrix(dim1[0])
            print("The result is:")
            print_matrix(transpose_vertical(transpose_horizontal(transpose_diag_main(matrix1))))
            del (dim1, matrix1)
        elif command_transpose == 3:
            # Vertical transpose
            dim1 = [int(x) for x in input("Enter matrix size: ").split()]
            print("Enter matrix:")
            matrix1 = get_matrix(dim1[0])
            print("The result is:")
            print_matrix(transpose_vertical(matrix1))
            del (dim1, matrix1)
        elif command_transpose == 4:
            # Horizontal transpose
            dim1 = [int(x) for x in input("Enter matrix size: ").split()]
            print("Enter matrix:")
            matrix1 = get_matrix(dim1[0])
            print("The result is:")
            print_matrix(transpose_horizontal(matrix1))
            del (dim1, matrix1)
    elif command == 5:
        # Calculate determinant
        dim1 = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        matrix1 = get_matrix(dim1[0])
        print("The result is: \n", determinant(matrix1), sep="", end="\n\n")
        del (dim1, matrix1)
    elif command == 6:
        # Calculate inverse of matrix
        dim1 = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        matrix1 = get_matrix(dim1[0])
        print("The result is:")
        print_matrix(inverse(matrix1))
        del (dim1, matrix1)
