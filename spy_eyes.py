from random import randint
import os, sys


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


p = 0
X = []
Y = []

for i in range(1, 10):
    # print(i + 1)
    n1 = get_random_number() + 3
    n2 = get_random_number() + 3

    X.append(n1)
    Y.append(n2)

erase_screen()

print(X)
print(Y)
