def writing(size_message, matrix_message):
    n, m = map(int, input(size_message).split())
    matrix = []
    print(matrix_message)
    for k in range(n):
        matrix.append(list(map(float, input().split())))
    return matrix, n, m


def matrix_print(A):
    print("The result is:")
    for i in A:
        print(*i)


def add(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(A[i])):
            result[i].append(A[i][j] + B[i][j])
    return result


def const_mult(matrix, const):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            result[i].append(matrix[i][j] * const)
    return result


def matrix_mult(A, B):
    result = []
    for k in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[k].append([])
            result[k][j] = 0
            for l in range(len(B)):
                result[k][j] += A[k][l] * B[l][j]
    return result


def main_transpose(matrix):
    result = []
    n, m = len(matrix), len(matrix[0])
    for r in range(m):
        new_row = [matrix[c][r] for c in range(n)]
        result.append(new_row)
    return result


def side_transpose(A):
    result = []
    n, m = len(A), len(A[0])
    for r in range(m-1, -1, -1):
        new_row = [A[c][r] for c in range(n-1, -1, -1)]
        result.append(new_row)
    return result


def vert_transpose(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix


def horiz_transpose(matrix):
    matrix = matrix[::-1]
    return matrix


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    elif len(A) == len(A[0]) == 1:
        return A[0][0]
    for fc in indices:
        As = A.copy()
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]
        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det
    return total


def inverse(A):
    det = determinant_recursive(A)
    if det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        C = []
        for i in range(len(A)):
            C.append([])
            for j in range(len(A)):
                C[i].append(0)
        for fc in range(len(A)):
            for fr in range(len(A)):
                As = A.copy()
                del As[fr]
                height = len(As)
                for i in range(height):
                    As[i] = As[i][0:fc] + As[i][fc+1:]
                sign = (-1) ** (fc + fr)
                C[fr][fc] = sign * determinant_recursive(As)
        return const_mult(main_transpose(C), det ** (-1))


def choice(num):
    if num == 1:
        A, n1, m1 = writing("Enter first matrix size: ", "Enter first matrix:")
        B, n2, m2 = writing("Enter second matrix size: ", "Enter second matrix:")
        if n1 == n2 and m1 == m2:
            matrix_print(add(A, B))
        else:
            print('The operation cannot be performed.')
    elif num == 2:
        A, n, m = writing("Enter matrix size: ", "Enter matrix:")
        const = float(input('Enter constant:'))
        matrix_print(const_mult(A, const))
    elif num == 3:
        A, n1, m1 = writing("Enter first matrix size: ", "Enter first matrix:")
        B, n2, m2 = writing("Enter second matrix size: ", "Enter second matrix:")
        if m1 == n2:
            matrix_print(matrix_mult(A, B))
        else:
            print('The operation cannot be performed.')
    elif num == 4:
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        chs = int(input("Your choice:"))
        if chs == 1:
            A, n, m = writing("Enter matrix size: ", "Enter matrix:")
            matrix_print(main_transpose(A))
        elif chs ==2:
            A, n, m = writing("Enter matrix size: ", "Enter matrix:")
            matrix_print(side_transpose(A))
        elif chs == 3:
            A, n, m = writing("Enter matrix size: ", "Enter matrix:")
            matrix_print(vert_transpose(A))
        elif chs == 4:
            A, n, m = writing("Enter matrix size: ", "Enter matrix:")
            matrix_print(horiz_transpose(A))
        else:
            print("Error")
    elif num == 5:
        A, n, m = writing("Enter matrix size: ", "Enter matrix:")
        if n != m:
            print('matrix is not square')
        else:
            print(f"The result is:\n {determinant_recursive(A)}")
    elif num == 6:
        A, n, m = writing("Enter matrix size: ", "Enter matrix:")
        if n != m:
            print('matrix is not square')
        else:
            matrix_print(inverse(A))
    elif num == 0:
        return 'exit'
    else:
        print("ERROR")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    if choice(int(input("Your choice:"))) == 'exit':
        break

