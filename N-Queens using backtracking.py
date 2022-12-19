import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import copy
import random


root = Tk()
root.title("N-Queens Problem Solver")
root.config(bg='#116562')

style = ttk.Style()
style.theme_use('classic')

board = ttk.Frame(root)
board.pack()
board.config(width=500, height=0, relief=RIDGE)
board = ttk.Frame(root)
board.pack()
board.config(width=0, height=0, relief=RIDGE)


def build_board(chrome):
    counter = 0
    for i in chrome:
        for n in range(len(chrome)):
            if counter % 2 == 0:
                if n % 2 == 0:
                    if n == i - 1:
                        ttk.Label(board, background='#b86006', text='♛', font=("?", 30), anchor="center").grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label(board, background='#b86006', text='        ').grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                else:
                    if n == i - 1:
                        ttk.Label(board, background='#F9E3B1', text='♛', font=("?", 30), anchor="center").grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label(board, background='#F9E3B1', text='        ').grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
            else:
                if n % 2 == 0:
                    if n == i-1:
                        ttk.Label(board, background='#F9E3B1', text='♛', font=("?", 30), anchor="center").grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label(board, background='#F9E3B1', text='        ').grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                else:
                    if n == i-1:
                        ttk.Label(board, background='#b86006', text='♛', font=("?", 30), anchor="center").grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
                    else:
                        ttk.Label(board, background='#b86006', text='        ').grid(
                            row=n, column=counter, sticky='snew', ipadx=160/len(chrome), ipady=160/len(chrome))
        counter += 1
solutions = []
def run(n):
    
    def get_board(n):
        #Returns an n by n board
        board = ["x"]*n
        for i in range(n):
            board[i] = ["x"]*n
        return board


    def solve(board, col, n):
        #Use backtracking to find all solutions
        if col >= n:
            return
        
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = "Q"
                if col == n-1:
                    add_solution(board)     
                    board[i][col] = "x"
                    return
                solve(board, col+1, n) #recursive call
                #backtrack
                board[i][col] = "x"
                
    def is_safe(board, row, col, n):
        #Check if it's safe to place a queen at board[x][y]
        #check row on left side
        for j in range(col):
            if board[row][j] == "Q":
                return False
        
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i=i-1
            j=j-1
        
        x, y = row,col
        while x < n and y >= 0:
            if board[x][y] == "Q":
                return False
            x=x+1
            y=y-1
        
        return True

    def add_solution(board):
        #Saves the board state to the global variable: solutions
        global solutions
        saved_board = copy.deepcopy(board)
        solutions.append(saved_board)


    #Returns a square board of nxn dimension
    board = get_board

    #Empty list of all possible solutions

    #Solving using backtracking
    solve(board, 0, n)

    def print_solution():
        #Prints one of the solutions randomly
        x = random.randint(0,len(solutions)-1) #0 and len(solutions)-1 are inclusive
        ans = []
        for mat in solutions[x]:
            for i in range(len(mat)):
                if mat[i] == 'Q':
                    ans.append(i + 1)
                    break
        return ans

    return print_solution()

def play():
    size = ent.get()
    if (size == ''):
        msg = 'error, please enter the size'
        tkinter.messagebox.showinfo('error', msg)
    elif (size.isnumeric() != True):
        msg = 'error, please enter number not else'
        tkinter.messagebox.showinfo('error', msg)
    elif (int(size) < 4 and int(size) != 1):
        msg = 'Sorry, no solution'
        tkinter.messagebox.showinfo('error', msg)
    else:
        chrome = run(int(size))
        print(chrome)
        build_board(chrome)


text = Label(root, text='Enter the size of the board')
ent = Entry(root)
btn = Button(root, text="enter", command=play)

text.pack()
ent.pack()
btn.pack()
btn.config(command=lambda: [restart_program(), play()])


# -: To restart the program :- #
def restart_program():
    for label in board.grid_slaves():
        label.grid_forget()
root.mainloop() 
