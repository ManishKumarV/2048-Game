import random
def start_game():
    mat = [[0 for x in range(4)] for y in  range(4)]
    return mat

def game_status(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==2048:
                return 'WIN'
    
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return 'NOT OVER'
    
    return 'LOSE'

def add_new_2(grid):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while grid[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    grid[r][c]=2

def reverse(grid):
    for i in range(4):
        for j in range(2):
            grid[i][j],grid[i][3-j]=grid[i][3-j],grid[i][j]
    return grid

def transpose(grid):
    for i in range(4):
        for j in range(i+1,4):
            grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
    return grid

def compress(grid):
    new_mat=[[0 for i in range(4)] for j in range(4)]
    change =False
    for i in range(4):
        pos=0
        for j in range(4):
            if grid[i][j]!=0:
                new_mat[i][pos]=grid[i][j]
                pos+=1
                if j!=pos and change  == False:
                    change =True
    return new_mat,change     

def add(grid):
    change=False
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                grid[i][j]*=2
                grid[i][j+1]=0
                if change == False:
                    change =True
    return grid,change

def move_left(grid):
    grid,change1 = add(grid)
    grid,change2 = compress(grid)
    change=change1 or change2
    return grid,change

def move_right(grid):
    grid=reverse(grid)
    grid,change1=add(grid)
    grid,change2=compress(grid)
    change=change1 or change2
    grid=reverse(grid) 
    return grid,change

def move_up(grid):
    grid=transpose(grid)
    grid,change1 = add(grid)
    grid,change2 = compress(grid)
    change=change1 or change2
    grid=transpose(grid)
    return grid,change

def move_down(grid):
    grid=transpose(grid)
    grid=reverse(grid)
    grid,change1=add(grid)
    grid,change2=compress(grid)
    change=change1 or change2
    grid=reverse(grid)
    grid=transpose(grid)
    return grid,change