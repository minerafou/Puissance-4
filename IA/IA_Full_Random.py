import random
class IAFullRandom():
    def __init__(self):
        self.name = "Random"
    def Calc(self, grid):
        while True:
            choice = random.randint(0,6)
            if grid[choice][5] == 0:
                return choice

