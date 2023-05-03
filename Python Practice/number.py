### Runtime Errors

"""
x = int(input("What is x? "))
print(f"x is {x}")
"""

## Try and except user input tests
"""
try:
    x = int(input("What is x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
"""

## running try in the fewest lines of code
"""
try:
    x = int(input("What is x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
"""

## Same as above but with included "else" statement
"""
try:
    x = int(input("What is x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
"""

## Improved code from above
"""
while True:
    try:
        x = int(input("What is x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
"""

## Using functions to get an integer
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x>"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
main()
"""

## Improving above code - Using functions to get an integer
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
"""

## Same as above code but fewer lines
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x?"))
        except ValueError:
            print("x is not an integer")

main()
"""

## "Pass" - makes it so code does not warn user
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x?"))
        except ValueError:
            pass

main()
"""

## further code refinement - "prompt" that user can see when asked for input

def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()