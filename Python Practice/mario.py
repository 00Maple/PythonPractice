### Textual representation of Mario

"""
print("#")
print("#")
print("#")
"""

## Improved code
"""
for _ in range(3):
    print("#")
"""

## Improving code with functions
"""
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
main()
"""

## Printing a horizontal row

"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
"""

## Printing rows and columns with functions
"""
def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        
        # For each brick in row
        for j in range(size):
        
        # Print brick
            print ("#", end="")
    #print blank line
        print()
main()
"""

## condensing previous code

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)
        
def print_row(width):
    print("#" * width)
main()