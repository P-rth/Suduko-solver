puzzle = [[0,0,7,  0,4,0,  0,0,0],
          [0,0,0,  0,0,8,  0,0,6],
          [0,4,1,  0,0,0,  9,0,0],
         
          [0,0,0,  0,0,0,  1,7,0],
          [0,0,0,  0,0,6,  0,0,0],
          [0,0,8,  7,0,0,  2,0,0],
         
          [3,0,0,  0,0,0,  0,0,0],
          [0,0,0,  1,2,0,  0,0,0],
          [8,6,0,  0,7,0,  0,0,5]]




#function to find empty space
def findnextempty():
  for y in range(9):
      for x in range(9):
        if puzzle[y][x] == 0:
          return y, x 
          
  return None, None

def check_valid(num,y,x):
    #check horizontal
    for i in range(0,9):
        if puzzle[y][i] == num:
            return False
    #check vertical
    for i in range(0,9):
        if puzzle[i][x] == num:
            return False
    #take the start points of the blocks (in index location)   
    blockstartx = (x//3)*3
    blockstarty = (y//3)*3
    #check Block for num
    for a in range (3):         # The sub-grid or block  ____\   Check if any of the  
        for b in range(3):      # has 3x3 grid               /   values of the subgrid maches num
            if puzzle[blockstarty+a][blockstartx+b] == num:
                return False
    return True     #all checks passed



#####################################################################################
#################### Solving the sudoku  ###########################################
###################################################################################


def solve():
  y,x = findnextempty()
  #print(y,x)
  if y is None:
    return True
    
  for i in range (1,10):
    
    if check_valid(i,y,x):
      
      puzzle[y][x] = i
      
      if solve() == True:
        return True
        
    puzzle[y][x] = 0 #not valid

solve()
print(puzzle)