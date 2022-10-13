import random
import copy
from addition import IsWin
class IAProbaV2():
    def __init__(self):
        self.name = "Proba V2"
    def GetName(self):
        return self.name
    def AddTokenTemp(self, grid_original, line, turn):
        for i in range(6):
            if grid_original[line][i] == 0:
                grid_original[line][i] = turn
                break
    def Simu(self, grid, turn):
        maxi = 10
        count = 0
        end = False
        IA_play = turn
        while not end:
            count += 1
            if turn == 1:
                turn = 2
            else:
                turn = 1
            while True:
                choice = random.randint(0, 6)
                if grid[choice][5] == 0:
                    break
            self.AddTokenTemp(grid, choice, turn)
            temp_winner = IsWin(grid)
            if temp_winner == IA_play:
                score = 2**(maxi-count)
                end = True
            elif temp_winner != None:
                score = -(2**(maxi-count))
                end = True
            elif grid[0][5] != 0 and grid[1][5] != 0 and grid[2][5] != 0 and grid[3][5] != 0 and grid[4][5] != 0 and grid[5][5] != 0 and grid[6][5] != 0:
                score = 0
                end = True
            elif count == maxi:
                score = 0
                end = True
        return score
    def Calc(self, original_grid, turn):
        best = None
        depth = 75
        best_line = 0
        for i in range(7):
            grid = copy.deepcopy(original_grid)
            if grid[i][5] != 0:
                continue
            self.AddTokenTemp(grid, i, turn)
            if IsWin(grid) != None:
                return i
            if grid[0][5] != 0 and grid[1][5] != 0 and grid[2][5] != 0 and grid[3][5] != 0 and grid[4][5] != 0 and grid[5][5] != 0 and grid[6][5] != 0:
                return i
            score = 0
            for j in range(depth):
                score += self.Simu(copy.deepcopy(grid), turn)
            print(score)
            if best == None or best < score:
                best = score
                best_line = i
        return best_line
        
    