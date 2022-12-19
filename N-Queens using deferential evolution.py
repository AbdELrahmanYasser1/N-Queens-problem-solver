import tkinter.messagebox
from tkinter import *
from tkinter import ttk
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

# -:CODE:- #
def run(NQueen):
    maxFitness = (NQueen * (NQueen - 1)) / 2 # 1 1 1 1 
    population = [generateChromosome(NQueen) for _ in range(100)]

    generation = 1

    # while maxFitness not found in population // 6 - (H + R + L)
    while not maxFitness in [fitness(chrom, maxFitness) for chrom in population]:
        population = Differential(population, fitness, maxFitness)
        generation += 1

    for chrom in population:
        if fitness(chrom, maxFitness) == maxFitness:
            print(f"Chromosome : {chrom}")
            print(f"The number of generation is : {generation}")
            print("-----------------------------------")
            return chrom
            

# -: Algorithm :- #

def generateChromosome(NQueen):
    List = []
    for _ in range(NQueen): 
        List.append(random.randint(1, NQueen))
    return List # 


def mutation(chromosome):
    # change the value of a random index in chromosome.
    n = len(chromosome)
    index = random.randint(0, n - 1)
    value = random.randint(1, n)
    chromosome[index] = value
    return chromosome


def crossover(chromosomex, chromosomey):
    # reproduce new chromosome from two Chromosomes.
    n = len(chromosomex)
    index = random.randint(0, n - 1)
    return chromosomex[0:index] + chromosomey[index:n]  


def fitness(chromosome, maxFitness):
    # calculate fitness for chromosome.
    # Global variables
    n = len(chromosome)
    left_diagonal = 0
    right_diagonal = 0
    horizontal_collisions = 0
    column = 0
    row = 0
    #
    # 1 1 2 1

    # horizontal_collisions
    for col in range(n): # 3 1 4 3
        column = col + 1 # next_column
        while column < n:
            if chromosome[col] == chromosome[column]:
                horizontal_collisions += 1
            column += 1
    #

    # left_diagonal_collisions
    for col in range(n):
        column = col + 1 # next_column
        row = chromosome[col] + 1 # next_row
        while column < n and row <= n:
            if row == chromosome[column]:
                left_diagonal += 1
            column += 1
            row += 1
    #

    # right_diagonal_collisions
    for col in range(n):
        column = col + 1 # next_column
        row = chromosome[col] - 1 # prev_row
        while column < n and row >= 1:
            if row == chromosome[column]:
                right_diagonal += 1
            column += 1
            row -= 1
    #
    return maxFitness - (horizontal_collisions + left_diagonal + right_diagonal) # 


def probability(chromosome, fitness, maxFitness):
    return fitness(chromosome, maxFitness) / maxFitness


def randomChromosome(population, probabilities):
    # pick random chrosome, based on probability
    sum = 0
    for i in range(len(population)):
        sum += probabilities[i]

    prop = random.uniform(0, sum)  # random probability
    prev = 0
    for a, b in zip(population, probabilities): 
        if prev + b >= prop:
            return a  # chromosome with hiegher probability
        prev += b  # sum of all previous probabilities



def Differential(population, fitness, maxFitness):
    new_population = []
    probabilities = [probability(chrom, fitness, maxFitness) for chrom in population]

    for _ in range(len(population)):
        x = randomChromosome(population, probabilities) #Best Chrom1
        y = randomChromosome(population, probabilities) #Best Chrom2

        child = mutation(x)
        child = crossover(child, y)
        

        if fitness(child, maxFitness) < fitness(x, maxFitness): # selection
            child = x

        new_population.append(child)
        if fitness(child, maxFitness) == maxFitness:
            break

    return new_population  # new generation


# -: Board Design :-#
# 3 1 4 2
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

# -: End Design :- #


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
