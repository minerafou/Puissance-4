import random
class IAFullLeft():
    def __init__(self):
        self.name = "Full left"
    def Calc(self, grid, turn):
        for i in range(7):
            if grid[i][5] == 0:
                return i
    def GetName(self):
        return self.name