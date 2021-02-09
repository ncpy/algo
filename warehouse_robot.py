import numpy as np
row = 10
col = 10

# at beginning
grid = np.zeros((row, col))

x = 1
y = 5
grid[y][x] = 1
grid[5][5] = -100
grid[0][9] = -100

step = 1
def N(step, y, x):
    step += 1
    grid[y-1][x] = step
    y = y-1
    return step, y, x

def S(step, y, x):
    step += 1
    grid[y+1][x] = step
    y = y + 1
    return step, y, x

def E(step, y, x):
    step += 1
    grid[y][x+1] = step
    x = x + 1
    return step, y, x

def W(step, y, x):
    step += 1
    grid[y][x-1] = step
    x = x - 1
    return step, y, x

liste = 'NENWNEYG'

for i in range(len(liste)):
    if liste[i] == "N":
        step, y, x = N(step, y, x)
    if liste[i] == "S":
        step, y, x = S(step, y, x)
    if liste[i] == "E":
        step, y, x = E(step, y, x)
    if liste[i] == "W":
        step, y, x = W(step, y, x)
print(grid)