from random import randint
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


def display_grid(GRID, positions):
    for cell in GRID:
        print(cell, end=" ")
    print("")


def get_random_number():
    return randint(1, 9)


def check_keyboard_input():
    pressed_key = keyboard.read_event()
    if pressed_key.event_type == keyboard.KEY_DOWN:
        return pressed_key


GRID_SIZE = 12
GRID = [(col, row) for row in range(GRID_SIZE) for col in range(GRID_SIZE)]

points = 0
positions = []

# Choose positions for the numbers
for i in range(9):
    positions.append([get_random_number() + 3, get_random_number() + 3])

erase_screen()
print(positions)

# Choose a random number
M = get_random_number()
display_grid(GRID, positions)

# while True:
#     I = check_keyboard_input()
#     if I:
#         print(I)
#     break
