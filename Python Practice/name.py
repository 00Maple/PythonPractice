### Using sys to print arguments from the Command-Line

## Using sys.argv
"""
import sys

print("hello, my name is", sys.argv[1])
"""
## Using IndexError to provide feedback if no text is entered in the command line
"""
import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""

## Improving the code - to be more defensive so user inputs correct values
"""
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
"""

## improving code using sys.exit
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
"""

## Taking a list with "slice" and tell compiler where we want to consider start and end of list

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# add [1:] after sys.argv and before the second ":" to omit entry 0 in the list