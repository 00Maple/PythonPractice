### Regular expressions

## Email verification basic
"""
email = input("What is your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
"""

## Email verification more specific
"""
email = input("What is your email? ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")
"""

## Email verification - improved logic
"""
email = input("What is your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""

## Email verification - import python "re" library
"""
import re

email = input("What is your email? ").strip()

if re.search("@", email):
    print("valid")
else:
    print("invalid")
"""

## Email Verification - Improved validation
"""
import re 

email = input("What is your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email verification - More aggressive validation
"""
import re

email = input("What is your email? ").strip()

if re.search(".+@.+.edu", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email verification - More logical aggressive validation using "\." interpreter treated as a literal "."
"""
import re

email = input("What is your email? ").strip()

if re.search(".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email Verification - More logical, treat string as raw string with "r"
"""
import re

email = input("What is your email?").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email verification - As above, further improved
"""
import re

email = input("What is your email?").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email verificaton - as above, improved more
"""
import re

email = input("What is your email?").strip()

if re.search(r"^[^@]+@[^@]=\.edu", email):
    print("Valid.")
else:
    print("Invalid")
"""

## Email Verification - narrow down to characters used in a sentence
"""
import re

email = input("What is your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_].+\.edu", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email Verification - regular expressions
"""
\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character
"""
"""
import re

email = input("What is your email? ").strip()

if re.search(r"^\w+@\w.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
"""

## Email verification - expand to allow other domains
"""
import re

email = input("What is your email? ").strip()

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
"""

### CASE SENSITIVITY
"""
import re

email = input("What is your email? ").strip()

if re.search(r"^\w+@\w.+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
"""

## Above code further improved to allow ffr @xxx.xxx.edu doman addresses

import re

email = input("What is your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    
## (\w+\.)? tells interpreter that the new expression can be there once, or not at all