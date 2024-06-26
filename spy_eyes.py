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


def get_random_number():
    return randint(1, 9)


def check_keyboard_input():
    pressed_key = keyboard.read_event()
    if pressed_key.event_type == keyboard.KEY_DOWN:
        return pressed_key


p = 0
X = []
Y = []

for i in range(1, 10):
    # print(i + 1)
    n1 = get_random_number() + 3
    n2 = get_random_number() + 3

    X.append(n1)
    Y.append(n2)

# erase_screen()

while True:
    I = check_keyboard_input()
    if I:
        print(I)
    break

# print(X)
# print(Y)
