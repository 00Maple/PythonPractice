### Extracting User Input

## extracting information from user input
"""
url = input("URL: ").strip()
print(url)
"""
## Extracting information from user input - extract username

"""
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
"""

# use .replace to tell interpreter to find one item and replace it with another

## Same as above code - improved
"""
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")
"""
## Improved code above using .sub expression
"""
import re
url = input("URL: ").strip()

username = re.sub("https://twitter.com/", "", url)
print(f"Username: {username}")
"""

## Further improved code above to account for differences in user input
"""
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
"""

## Altered code to use .search expression instead of .sub
"""
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"Username:", matches.group(2))
"""
# above code does not work as well as lines 37 - 42 at extrapolating username from URL

## improved code from above lines 47-54
"""
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
"""

## improved above code to look for word characters

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))