from random import randint
from turtle import pos
import keyboard, os, sys


def verify_os():
    if sys.platform == "win32" or sys.platform == "cygwin":
        erasecmd = "cls"
    else:
        erasecmd = "clear"
    return erasecmd


def erase_screen():
    clearcmd = verify_os()
    os.system(clearcmd)


def check_keyboard_input():
    pressed_key = keyboard.read_event()
    if pressed_key.event_type == keyboard.KEY_DOWN:
        return pressed_key


# Initialize the variable for the positions of the numbers that are going to be displayed on the screen and sets it's values
def get_random_positions(numbers_list_size):
    positions = set()
    while len(positions) < numbers_list_size:
        row = randint(0, GRID_SIZE - 1)
        col = randint(0, GRID_SIZE - 1)
        positions.add((row, col))
    return positions


def create_grid():
    return [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def set_numbers_positions():
    for number, position in zip(numbers, positions):
        row, col = position
        grid[row][col] = number


def display_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


# Define the size of the Grid
GRID_SIZE = 12

# Calls the function that creates the Grid
grid = create_grid()

# Create the list with all the 9 numbers, from 1 to 9, that are going to be displayed on the screen
numbers = list(range(1, 10))

# Choose positions for the numbers
positions = get_random_positions(len(numbers))

set_numbers_positions()

erase_screen()

# Display the grid on the screen
display_grid(grid)

# I = check_keyboard_input()
