'''
Department of Electrical Engineering and Computer Science
Texas A&M University-Kingsville
CSEN 5303 Foundations of Computer Science
Fall 2022
Instructor: Habib M. Ammari, Ph.D. (CSE), Ph.D. (CS)
Student: Nickolas Rodriguez
Project 1: Design, Analysis, and Implementation of Game of Life
Due Date: Sep. 23, 2022
'''

import numpy as np
import random

def generate_grid(row_x, col_y):
    '''
    Function that generates a grid of size (row_x, col_y).
    Adds two rows and columns of 0s for padding.
    Returns the padded grid.
    '''
    random.seed(11) # set random seed
    total = row_x*col_y # total number of available cells

    # Acquire the number of alive and dead cells to generate.
    rand_x = random.randrange(0, total)
    rand_y = total - rand_x

    # Create a list of alive (1) and dead (0) cells. Convert to an array and shuffle.
    base_list = [0]*rand_x + [1]*rand_y
    base = np.array(base_list, dtype=np.uint8)
    np.random.shuffle(base)

    # Reshape the array based on the inputted dimensions. Add two rows and columns for padding.
    pre_grid = np.reshape(base, (row_x, col_y))
    grid = np.pad(pre_grid, (1,), 'constant', constant_values=(0))

    return grid

def GameOfLife(grid):
    
    row = grid.shape[0] # total number of rows
    col = grid.shape[1] # total number of columns

    # Create an empty array (next_gen) of the same shape.
    next_gen = np.array([0]*row*col, dtype=int)
    next_gen = np.reshape(next_gen, (row, col))

    for x in range(1, row-1): # Loop through only available rows. Skip padding.
        for y in range(1 ,col-1): # Loop through only available columns. Skip padding.
            # Order of operations for all 8 surrounding cells.
            x_list = [-1, -1, -1, 0, 0 ,1, 1 ,1]
            y_list = [-1, 0, 1, -1, 1, -1 ,0 ,1]
            target = grid[x, y] # Current dead/live cell.
            total = 0 # Reset total
            for z in range(len(x_list)): # Loop through list of operations.
                # Find total number of alive cells based on list of operations. Always 8 to check.
                total = total + grid[x+x_list[z], y+y_list[z]]

            if(target == 1 and 2 <= total <= 3):
                # Live cell w/ 2 or 3 neighbours, survives.
                next_gen[x,y] = 1
            elif(target == 0 and total == 3):
                # Dead cell w/ 3 neighbours, gives birth.
                next_gen[x,y] = 1
            else:
                # All other types of cells die.
                next_gen[x,y] = 0

    return next_gen
