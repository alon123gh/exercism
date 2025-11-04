
def validate(matrix):
    if any (len(row) != len(matrix[0])  for row in matrix):
        raise ValueError("irregular matrix")

def saddle_points(matrix):

    validate(matrix)
    if not matrix:
        return []
    columns = []
    for i in range (len(matrix[0])):
        columns.append([row[i] for row in matrix ])

    result = []
    for x in range(len(matrix)):
        for y in range(len(columns)):
            tree = matrix[x][y]
            if tree == max(matrix[x]) and tree == min(columns[y]):
                result.append({"row": x+1, "column": y+1})

    return result