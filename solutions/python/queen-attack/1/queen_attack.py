class Queen:


    def __init__(self, row, column):
        self.row = row
        self.column = column

        self.validate()

    def validate(self):

       coordinates = {"row" : self.row,
                      "column": self.column}

       for  axis, value in coordinates.items():
           if value < 0 :
               raise ValueError(f"{axis} not positive")
           if value > 7:
               raise ValueError(f"{axis} not on board")

    @staticmethod
    def end_pos(direction_component):
         return  -1 if direction_component == -1 else 8

    def can_attack(self, another_queen):

        if another_queen.row == self.row and another_queen.column == self.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        if another_queen.row == self.row or another_queen.column == self.column:
            return True

        result = False
        directions = [(-1,-1), (-1,1),  (1,1), (1,-1)]
        for direction in directions :
            x_end = Queen.end_pos(direction[0])
            y_end = Queen.end_pos(direction[1])

            diagonal = list(zip (range(self.row+direction[0],x_end,direction[0]),
                            range(self.column+direction[1],y_end,direction[1])))
            if (another_queen.row, another_queen.column) in diagonal:
                result = True
        return result



