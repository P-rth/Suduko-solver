import time   #used to mesure how long the code took to execute
import threading  #display current bord without slowing down the main process
import os

def filledpercent():
  while solved != 1:
    os.system("cls || clear")
    board_printer(puzzle)
    


def board_printer(board):
    """Prints the sudoku board nicely"""

    for y in range(9):
        s = ''

        for x in range(9):
            s += str(board[y][x]) + ' '

            if not (x + 1) % 3:
                s += '| '

        print(s)

        if not (y + 1) % 3:
            print('-' * len(s))
  

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

#Take user input
'''
puzzle = [[5,0,1,  3,0,0,  0,0,0],
          [8,0,0,  0,0,8,  0,2,0],
          [0,7,0,  0,1,0,  5,0,0],
         
          [4,0,0,  0,0,5,  3,0,0],
          [0,1,0,  0,7,6,  0,0,6],
          [0,0,3,  2,0,0,  2,0,0],
         
          [0,6,0,  5,0,0,  0,0,9],
          [0,0,4,  0,0,0,  0,3,0],
          [8,6,0,  0,0,9,  7,0,0]]  
'''    
          
          
puzzle = []
for i in range(9):
  prp = "input row "+str(i+1)+":"
  x = input(prp)
  row = []
  if (len(x) > 9):
    print("Length of string entered is more than 9 will be trimed to first 9 numbers")
  if (len(x) < 9):
    print("Length of string is less the 9 numbers the remaining",9-len(x),"will be filled with zeros")
    x = x.ljust(10, '0')
  for j in range(9):
    abc = int(x[j])
    row.append(abc)
  puzzle.append(row)

            
###########################################################################
#########################################################################

#actully execute code

solved = 0
start = time.process_time()                       #start timer

t1 = threading.Thread(target=filledpercent)
t1.start()

rotated_puzzle = rotate_puzzle()
blocks = block_list()
if solve(rotated_puzzle, blocks):
    solved = 1
    execute_time=(time.process_time() - start)                #end timer
    time.sleep(1)
    os.system("cls || clear")
    print("Took",round(execute_time,4),"seconds to solve")
    print()
    board_printer(puzzle)
else:
    solved = 1
    time.sleep(1)
    os.system("cls || clear")
    execute_time=(time.process_time() - start)                #end timer
    print("Took",round(execute_time,4),"seconds")
    print("Puzzle is unsolveable!")
        
t1.join()               #wait for the thread to end 
