
grid=[]
ROWS=7      # alternatively, 9
COLUMNS=6   # 6
marker = "x"            #default marker at beginning
player = "Player 1"     #default player at beginning


for i in range(ROWS):       # create a ROWS-by-COLUMNS matrix
    col = []
    for j in range(COLUMNS):
        col.append(".")
    grid.append(col)

def checkRows(grid, marker):
    for i in range(len(grid)):      # for every row in a grid
        for j in range(len(grid[i])):   # for every column(or item) in row
            if j < len(grid[i])-3:   #check horizontaly
                if grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == marker:
                    return True

            if i < len(grid)-3:     #check vertically
                if grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j] == marker:
                    return True

            if  i < len(grid)-3 and j < len(grid[i])-3:     #check diagonal (left-up to right-down)
                if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == marker:
                    return True

            if  i < len(grid)-3 and j < len(grid[i])+3:     #check diagonal (left-down to right-up)
                if grid[i][j] == grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] == marker:
                    return True

def is_available(item_row, play_col):   #check if column(item) in row is available
    if item_row[play_col] == '.':
        return True
    return False

def play(grid, play_col, marker, player):
    for item_row in reversed(grid):
        if is_available(item_row, play_col-1):
            item_row[play_col-1] = marker
            is_true = checkRows(grid, marker)
            if is_true: # game over
                return marker, player, True

            if marker == "o":
                marker ="x"
                player = "Player 1"
            else:
                marker ="o"
                player = "Player 2"
            return marker, player, False
    return marker, player, False
    
while True:
    for i in grid:
        print(i, sep="\n")
    print(player, "choose a number 1-6: ")
    play_col = input()
    if play_col.isnumeric():
        play_col = int(play_col)
        if 0<play_col<7 :
            marker, player, is_winner = play(grid, play_col, marker, player)

            if is_winner:  # exit the game
                for i in grid:      # it's for result-show
                    print(i, sep="\n")
                print(player, " with ", marker, " won!")
                break       # no more game, when winner has declared
