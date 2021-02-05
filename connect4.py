
ROWS=7
COLUMNS=6
marker = "x"

# i = 1
# while i < 10:
#     #print(i)
#     if i == 5:
#         i += 1
#     i += 1

grid=[]

for i in range(ROWS):
    col = []
    for j in range(COLUMNS):
        col.append(".")
    grid.append(col)


def checkRows(marker, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j < len(grid[i])-2:
                if grid[i][j] == grid[i][j+1] == grid[i][j+2] == marker:
                    print("Player horiz "+marker+ " won!")
                    return True

            if i < len(grid)-2:
                if grid[i][j] == grid[i+1][j] == grid[i+2][j] == marker:
                    print("Player verti "+marker+ " won!")

            if  i < len(grid)-2 and j < len(grid[i])-2:
                if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == marker:
                    print("Player diagonal + "+marker+ " won!")

            if  i < len(grid)-2 and j < len(grid[i])+2:
                if grid[i][j] == grid[i+1][j-1] == grid[i+2][j-2] == marker:
                    print("Player diagonal - "+marker+ " won!")

def play(grid, play_col, marker):
    for item_row in reversed(grid):
        if is_available(item_row, play_col-1):
            item_row[play_col-1] = marker
            checkRows(marker, grid)

            if marker == "o":
                marker ="x"
            else:
                marker ="o"
            return marker
    return marker
            
def is_available(item_row, play_col):  
    if item_row[play_col] == '.':
        return True
    return False
    
while True:
    for i in grid:
        print(i, sep="\n")
    play_col = input("Which column? ")

    print(play_col)
    if play_col.isnumeric():
        if 0<int(play_col)<7 :
            marker = play(grid, int(play_col), marker)