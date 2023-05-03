### Loops

## print loop

#print("meow")
#print("meow")
#print("meow")

## While loop

"""
i = 3
while i != 0:
    print("meow")
    i = i - 1 # to prevent infinite loops
"""

## While loop counting from zero

"""
i = 0
while i < 3:
    print("meow")
    i += 1 
"""
# += is the same as saying i = i + 1

# For loops
"""
for i in [0, 1, 2]:
    print("meow")
"""

# Improved loop
"""
for i in range(3):
    print("meow")
"""
# Loop further improved, adding "_" functions the same as "i"
"""
for _ in range(3):
    print("meow")
"""

# Loop further improved/condensed - no line breaks
"""
print("meow" * 3)    
"""

# Loop improved again with line breaks
"""
print("meow\n" * 3, end="")
"""

# Loop improved with User Input
"""
while True:
    n = int(input("What is n?"))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")
"""

# Improved code - Remove redundant continue keyword
"""
while True:
    n = int(input("What is n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""

# Defining functions to improve code

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

# Execute code
main()