### File I/O
"""
name = input("What is your name?" )
print(f"hello", {name})
"""
## Creating a names list
"""
names = []

for _ in range(3):
    name = input("What is your name?" )
    names.append(name)
"""

## Simplified above code

"""
names = []

for _ in range(3):
    names.append(input("What is  your name?"))
"""
## enables the ability to print a list of names
"""
for name in sorted(names):
    print(f"hello", {name})
"""
## write names to a file, append with "a" and add line breaks with (f"{name}\n)
"""
name = input("What is your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""

## read from file
"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
"""

## read from file sorting names

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")