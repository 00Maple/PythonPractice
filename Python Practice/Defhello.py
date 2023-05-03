### Create your own functions

## Final code of hello.py lesson
# Ask user for their name, remove whitespcae, capitalize first letter of each word
#name = input("What's your name?").strip().title()

# Print the output
#print(f"hello, {name}")

## Defining functions
#def hello() :
#    print("hello")

#name = input("What's your name? ")
#hello()
#print(name)

## Improved Defining Functions code

# Defining a function - to Variable
#def hello(to) :
#    print("hello,", to)

# output using my own function
#name = input("What's your name?")
#hello(name)

## Add default value to "hello"

#def hello(to="world") :
#    print("hello,", to)

# Output using my own function
#name = input("What's your name?")
#hello(name)

# Output without passing the expected arguments
#hello()

## Defining separate functions

# Defining a "main" function
def main() : 
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    
    #output without passing the expected arguments
    hello()

#Create our own function
def hello(to="world") :
    print("hello,", to)    

main()