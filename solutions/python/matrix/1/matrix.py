class Matrix:
    def __init__(self, matrix_string):
        self.rows = Matrix.parse(matrix_string)
        self.columns =  [list(col) for col in zip(*self.rows)]

    @staticmethod
    def parse(matrix_string):
        rows_strings = matrix_string.split("\n")
        return [ list(map(int,rows_string.split())) for rows_string in rows_strings]

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]