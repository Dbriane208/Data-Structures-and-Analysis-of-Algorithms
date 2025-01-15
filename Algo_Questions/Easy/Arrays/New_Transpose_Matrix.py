# time O(w*h) | space O(w*h)
def transposeMatrix(matrix):
    transposedOutput = []

    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedOutput.append(newRow)

    return transposedOutput        
