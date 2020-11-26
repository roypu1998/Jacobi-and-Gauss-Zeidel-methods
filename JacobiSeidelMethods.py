import numpy as np
def createMatrix():
    row=int(input('enter numbers of row:'))
    lstMatrix=[]
    for i in range(0,row):
        matrix = []
        x=int(input(f'enter x for the {i+1} row : '))
        y=int(input(f'enter y for the {i+1} row : '))
        z=int(input(f'enter z for the {i+1} row : '))
        matrix.append(x)
        matrix.append(y)
        matrix.append(z)
        lstMatrix.append(matrix)
    return lstMatrix
def checkDiagonalMatrix(matrix):
    count=0
    for i in range(len(matrix)):
        sumOfrow = 0
        sumOfrow+=sum(matrix[i])
        result=sumOfrow-matrix[i][i]
        if result>matrix[i][i]:
            count+=1
    return count


def createVector():
    vector=[]
    print('enter 3 values to vector (x,y,z) : ')
    x = int(input(f'enter x to vector : '))
    y = int(input(f'enter y to vector : '))
    z = int(input(f'enter z to vector : '))
    vector.append(x)
    vector.append(y)
    vector.append(z)
    return vector

def jacobsMethod(matrix, vector, e, max_iterations):
    checkMatrix = checkDiagonalMatrix(matrix)
    if checkMatrix > 0:
        print("This matrix doesn't diagonal!!!!!")
    else:
        x = np.zeros_like(vector)
        for iter in range(max_iterations):
            print(f"{iter} ==>", x)
            x_new = np.zeros_like(x)

            for i in range(matrix.shape[0]):
                s1 = np.dot(matrix[i, :i], x[:i])
                s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
                x_new[i] = (vector[i] - s1 - s2) / matrix[i, i]

            if np.allclose(x, x_new, atol=e, rtol=0.):
                break

            x = x_new

        print(" ")
        print("Final approximation:")
        print(x)
        print(" ")
        error = np.dot(matrix, x) - b
        print("Final error:")
        print(error)



def zeidelMethod(matrix, vector, e, max_iterations):

    checkMatrix=checkDiagonalMatrix(matrix)
    if checkMatrix>0:
        print("This matrix doesn't diagonal!!!!!")
    else:
        x = np.zeros_like(vector)
        for iter in range(1, max_iterations):
            x_new = np.zeros_like(x)
            print(f"{iter} ==>{x}")
            for i in range(matrix.shape[0]):
                s1 = np.dot(matrix[i, :i], x_new[:i])
                s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
                x_new[i] = (vector[i] - s1 - s2) / A[i, i]
            if np.allclose(x, x_new, rtol=e):
                break
            x = x_new
        print(" ")

        print("Final approximation:")
        print(x)
        print(" ")
        error = np.dot(matrix, x) - vector
        print("Final error:")
        print(error)


A=np.array(createMatrix())
b = np.array(createVector())

zeidelMethod(A, b, 0.001, 20)
jacobsMethod(A, b, 0.001, 20)
