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

def findblock(y,x):
  blockx=(x//3)
  #relx=(index[1]%3)
  blocky=(y//3)
  #rely=(index[0]%3)


def readblock(y,x):
    out = []
    for a in range(3*y,(3*y)+3):       #y-axis
      for b in range(3*x,3+(3*x)):     #x-axis
        out.append(puzzle[a][b])
   # print (out)
    return out  
    

def read_y(x):
  out=[]
  for i in range(9):
    out.append(puzzle[i][x])
  return out

def read_x(y):
  out=[]
  for i in range(9):
    out.append(puzzle[y][i])
  return out 



#####################################################################################
#################### Solving the sudoku  ###########################################
###################################################################################


def check_valid(num,y,x):
  if num in readblock(y//3,x//3) or num in read_x(y) or num in read_y(x):
    return False
  else:
    return True



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
        
    puzzle[y][x] = 0

solve()
print(puzzle)