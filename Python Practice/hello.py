## Basic inefficient hello, world code
# Ask the user for their name
#name = input("What's your name? ")

# Print Hello
#print("hello, ")

# Print the name inputted
#print(name)

## prevent new line creation with end=
# Ask for users name
#name = input("What's your name?")

# Print hello and inputted name
#print("hello, " + name)

# Ask user for name
#name = input("What's your name?")
#print("hello,", end="")
#print(name)

## removing unnecessary spaces with .strip()
# Ask user for name
#name = input("What's your name?")
#print(f"hello, {name}")

# Ask the user for their name
#name = input("What's your name?")

# Remove Whitespace from the str
#name = name.strip()

# Print the output
#print(f"hello, {name}")

## automatic capitalization with .title()
# Ask user for their name
#name = input("What's your name?")

# Remove whitespace from str
#name = name.strip()

# Capitalize the first letter of each word

#name = name.title()

# Print the output
#print(f"hello, {name}")


## make code more efficient combining .strip() and title() in variable
# Ask user for name
#name = input("What's your name?")

# Remove whitespace and capitalize
#name = name.strip().title()

# Print output
#print(f"hello, {name}")

## increased efficiency
# Ask user for name, remove whitespace from the str and capitalize first letter of each word
"""
name = input("What's your name?").strip().title()

# Print output
print(f"hello, {name}")
"""
# Generates an exception
"""
print("hello, world) 
"""

def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()