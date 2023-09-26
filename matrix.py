def process_matrix(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]

    return matrix