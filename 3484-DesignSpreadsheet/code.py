class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet={}
        col = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(col)):
            self.spreadsheet[col[i]] = [0 for i in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.spreadsheet[col][row-1]=value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.spreadsheet[col][row-1]=0

    def getValue(self, formula: str) -> int:
        formula_clean = formula.strip("=").split("+")
        if formula_clean[0].isnumeric() == True and formula_clean[1].isnumeric() == True:
            return int(formula_clean[0])+int(formula_clean[1])
        if formula_clean[0].isnumeric() == False and formula_clean[1].isnumeric() == False:
            col0 = formula_clean[0][0]
            row0 = int(formula_clean[0][1:])-1
            col1 = formula_clean[1][0]
            row1 = int(formula_clean[1][1:])-1
            return self.spreadsheet[col0][row0]+self.spreadsheet[col1][row1]
        if formula_clean[0].isnumeric() == True and formula_clean[1].isnumeric() == False:
            col1 = formula_clean[1][0]
            row1 = int(formula_clean[1][1:])-1
            return int(formula_clean[0])+self.spreadsheet[col1][row1]
        if formula_clean[0].isnumeric() == False and formula_clean[1].isnumeric() == True:
            col0 = formula_clean[0][0]
            row0 = int(formula_clean[0][1:])-1
            return self.spreadsheet[col0][row0]+int(formula_clean[1])



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)