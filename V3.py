import time   #used to mesure how long the code took to execute



def findempty():
  global puzzle
  for y in range(9):
    for x in range(9):
      if puzzle[y][x] == 0:
        return y, x
  return None , None  #no empty space left on the puzzle
    

#rotate the puzzle to get the numbers in y-axis as lists
def rotate_puzzle():
  global puzzle
  out = []
  for y in range(9):
    out_x=[]
    for x in range(9):
      out_x.append(puzzle[x][y])   #x,y are swapped here because we want to rotate the puzzle
    out.append(out_x)
  return(out)

def block_list():
  global puzzle                                   #to make a list of all the blocks
  template_puzzle = [[0,0,0, 0,0,0, 0,0,0],
                     [0,0,0, 0,0,0, 0,0,0],
                     [0,0,0, 0,0,0, 0,0,0],
                     
                     [0,0,0, 0,0,0, 0,0,0],
                     [0,0,0, 0,0,0, 0,0,0],     #define a empty board as to fill in the values
                     [0,0,0, 0,0,0, 0,0,0],
                     
                     [0,0,0, 0,0,0, 0,0,0],
                     [0,0,0, 0,0,0, 0,0,0],
                     [0,0,0, 0,0,0, 0,0,0]]
  for y in range(9):
        for x in range(9):
          
            '''
            print("input",y,x)                       \
            print("##############################")  |
            rely=y%3                                 |       uncomment to check the
            relx=x%3                                 |       working of the below expression
            blockx=x//3                              |
            blocky=y//3                              |
            finaly=rely+3*(relx)                     |       (used for debugging)
            finalx=blocky+3*(blockx)                 |       
            print("y=",finaly,"x=",finalx)           |       sets the values in template_puzzle
            print("val =",puzzle[finaly][finalx])    |       in a given order by reading them
            print()                                  |       from the given puzzle
            print()                                  /                 /^\
            '''#                                                        |
               #                                                        
            template_puzzle[ (y//3)+(3*(x//3))   ][  (y%3)+(3*(x%3))   ] = puzzle[x][y]
  return template_puzzle
  

def valid(rotated_puzzle,block_list,num,y,x):
  global puzzle
  
  #row
  if num in puzzle[y]:
      return False          #repeated --> wrong guess
  
  #check column
  if num in rotated_puzzle[x]:
      return False
    
  # check block
  if num in block_list[ (x//3)+(3*(y//3)) ]:
      return False 
  


  return True




#########################################################################
#######################################################################

def solve(rotated_puzzle, block_list, x=0):
  global puzzle
  
  #find the next empty spot in the sudoku
  x, y = findempty()

  #check if there are no valid inputs
  if x is None:
      return True 
  
  # guess the number 
  for guess in range(1, 10):
    
      #check if the guessed number is valid for the position
      if valid(rotated_puzzle, block_list, guess, x, y):
        
          #if this is a valid guess insert it into puzzle
          puzzle[x][y] = guess
          rotated_puzzle[y][x] = guess
          block_list[y//3+3*(x//3)][y%3+3*(x%3)] = guess
          
          #recurse!
          if solve(rotated_puzzle, block_list,x):
              return True
      
  #if the guessed number is not valid reset the entered number and try again
  puzzle[x][y] = 0
  rotated_puzzle[y][x] = 0
  block_list[y//3+3*(x//3)][y%3+3*(x%3)] = 0
  #none of the numbers we tryed worked so this puzzle is unsolveable  --> return False
  return False
  
###################################################################################
##################################################################################
#actully execute code
start = time.process_time()                                 #start timer

puzzle = [[0,0,7,  0,4,0,  0,0,0],
          [0,0,0,  0,0,8,  0,0,6],
          [0,4,1,  0,0,0,  9,0,0],
         
          [0,0,0,  0,0,0,  1,7,0],
          [0,0,0,  0,0,6,  0,0,0],
          [0,0,0,  7,0,0,  2,0,0],
         
          [3,0,0,  0,0,0,  0,0,0],
          [0,0,0,  1,2,0,  0,0,0],
          [8,6,0,  0,7,0,  0,0,5]]



rotated_puzzle = rotate_puzzle()
blocks = block_list()
solve(rotated_puzzle, blocks)

execute_time=(time.process_time() - start)                #end timer
print("Took",round(execute_time,3),"seconds to solve")
print(puzzle)

