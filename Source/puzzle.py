from random import sample,choice,randint
from copy import deepcopy
from overloading import overload
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
        for _ in range(200):
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

    def clone(self):
        new_puzz= Generater_N_Puzzle(self.k)
        new_puzz.board= deepcopy(self.board)
        new_puzz.row_empty=self.row_empty
        new_puzz.col_empty=self.col_empty
        return new_puzz

class Depth_First_Search:
    @staticmethod
    def search(puzzle,leverdeep):
        if(leverdeep>LIMIT):
            return False,puzzle
        for i in range(4):
            if Action.Move(i,puzzle):
               
                if puzzle.UpdateScore()==puzzle.k**2:
                    return True,puzzle
                result,puzzle_child=Depth_First_Search.search(puzzle.clone(),leverdeep+1)
                if result:
                    return True,puzzle_child
                Action.Move((i+2)%4,puzzle)
        return False,puzzle
        
if __name__=='__main__':
    LIMIT=15
    puzzle=Generater_N_Puzzle(3)
    puzzle.generate_puzzle()
    puzzle.displayBoard()
    result,puzzle_child=Depth_First_Search.search(puzzle,0)
    if result:
        print("giai thanh cong!")
    else:
        print("giai that bai!")
    puzzle_child.displayBoard()

            


    


            
        

