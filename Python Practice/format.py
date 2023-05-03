### Cleaning up user input
"""
name = input("What is your name? ").strip()
print(f"hello, {name}")
"""
# Above works the same as the "hello, world" code but does not allow for "Lname, Fname" only one or the other

## Modified code to allow for "Lname, Fname" format
"""
name = input("What is your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
"""
## Modified above code including regular expression syntax
"""
import re

name = input("What is your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")
"""

## Modified above code to request for specific groups group(1), group(2) etc
"""
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")
"""
## Above code further cleaned up
"""
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
"""

## Further improved from code above

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")