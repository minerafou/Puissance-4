def IsWin(grid):
    #vertical
    for x in range(7):
        for y in range(3):
            first_color = grid[x][y]
            win = True
            for i in range(1, 4):
                if first_color != grid[x][y+i] or first_color == 0:
                    win = False
                    break
            if win:
                return first_color
    #horizontal
    for x in range(4):
        for y in range(6):
            first_color = grid[x][y]
            win = True
            for i in range(1, 4):
                if first_color != grid[x+i][y] or first_color == 0:
                    win = False
                    break
            if win:
                return first_color
    #diagonal bottom left
    for x in range(4):
        for y in range(3):
            first_color = grid[x][y]
            win = True
            for i in range(1, 4):
                if first_color != grid[x+i][y+i] or first_color == 0:
                    win = False
                    break
            if win:
                return first_color
    #diagonal bottom right
    for x in range(3, 7):
        for y in range(3):
            first_color = grid[x][y]
            win = True
            for i in range(1, 4):
                if first_color != grid[x-i][y+i] or first_color == 0:
                    win = False
                    break
            if win:
                return first_color
    return None