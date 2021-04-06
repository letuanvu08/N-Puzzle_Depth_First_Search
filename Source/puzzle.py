from random import sample,choice,randint
from copy import deepcopy
from overloading import overload
from time import time
UP=0
RIGHT=1
DOWN=2
LEFT=3
LIMIT=10000
class Action:
    @staticmethod
    def Move(direction,puzzle):
        if direction not in range(4):
            return False
        elif direction==UP:
            if puzzle.row_empty==0:
                return False
            else:
                Action.swap(puzzle,puzzle.row_empty-1,puzzle.col_empty)
                return True
        elif direction==DOWN:
            if puzzle.row_empty==puzzle.k-1:
                return False
            else:
                Action.swap(puzzle,puzzle.row_empty+1,puzzle.col_empty)
                return True
        elif direction==RIGHT:
            if puzzle.col_empty==puzzle.k-1:
                return False
            else:
                Action.swap(puzzle,puzzle.row_empty,puzzle.col_empty+1)
                return True
        elif direction==LEFT:
            if puzzle.col_empty==0:
                return False
            else:
                Action.swap(puzzle,puzzle.row_empty,puzzle.col_empty-1)
                return True
    @staticmethod
    def swap(puzzle,r,c):
        puzzle.board[puzzle.row_empty][puzzle.col_empty]=puzzle.board[r][c]
        puzzle.board[r][c]=0
        puzzle.row_empty=r
        puzzle.col_empty=c
class Generater_N_Puzzle:
    def __init__(self, k):
        self.k=k
        self.row_empty=0
        self.col_empty=0
        self.board=[]
        self.score=0
    def generate_puzzle(self):
        self.board=[[col for col in range(self.k*row,self.k*(row+1))] for row in range(self.k)]
        for _ in range(100*self.k):
            Action.Move(randint(0,3),self)
        return self.UpdateScore()
    def UpdateScore(self):
        self.score=0
        for i in range(self.k):
            for j in range(self.k):
                if i*self.k+j==self.board[i][j]:
                    self.score+=1
        return self.score
    def displayBoard(self):
        [print(row) for row in self.board]

class Depth_First_Search:
    @staticmethod
    def search(puzzle,leverdeep,preAction):
    
        if(leverdeep>LIMIT):
            return False
        for i in range(4):
            if (i+2)%4!=preAction and Action.Move(i,puzzle):
               
                if puzzle.UpdateScore()==puzzle.k**2:
                    return True
                if Depth_First_Search.search(puzzle,leverdeep+1,i):
                    return True
                Action.Move((i+2)%4,puzzle)
        return False
        
if __name__=='__main__':
    LIMIT=50
    puzzle=Generater_N_Puzzle(4)
    puzzle.generate_puzzle()
    puzzle.displayBoard()
    start=time()
    if Depth_First_Search.search(puzzle,0,-1):
        print("Successfully!")
    else:
        print("failed!")
    end=time()
    puzzle.displayBoard()
    print("Run times:"+str(int(end-start))+"s")

            


    


            
        

