## Modulo operator "%" - to see if two numbers divide evenly or have a remainder

# User input
#x = int(input("What's x? "))

#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

## Creating our own Parity function

# Defining main function
#def main():
#    x = int(input("What is x?"))
#    if is_even(x):
#        print("Even")
#    else:
#        print("Odd")

# Defining "is_even" function
#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

# Execute code
#main()

## Pythonic parity function

# Defining main function
#def main():
#    x = int(input("What is x?"))
#    if is_even(x):
#        print("Even")
#    else:
#        print("Odd")

# Defining "is_even" function
#def is_even(n):
#    return True if n % 2 == 0 else False

#main()

## Pythonic parity function - more readable

# Defining main function
#def main():
#    x = int(input("What is x?"))
#    if is_even(x):
#        print("Even")
#    else:
#        print("Odd")

# Defining "is_even" function
#def is_even(n):
#    return n % 2 == 0

# Execute code
#main()

## Match statements using if, elif, and else

# User input
#name = input(" What's your name? ")

#if name == "harry":
#    print("Gryffindor")
#elif name == "Hermoine":
#    print("Gryffindor")
#elif name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who the fuck are you???")

## Improved if, elif, else, or match statement

# User input
#name = input("What's your name? ")

#if name == "Harry" or name == "Hermoine" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who the fuck are you?")

## Match statements without if elif else

# User input
#name = input("What's your name? ")

# Case match statements
#match name:
#    case "harry":
#        print("Gryffindor")
#    case "Hermoine":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
#    case "Draco":
#        print("Slytherin")
#    case _:
#        print("WHO???")

## Improved case match statements

# User input
name = input("What's your name? ")

# Case match statements
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("WHO?")