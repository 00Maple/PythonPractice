### Using Libraries

## Using the Random module
"""
import random

coin = random.choice(["heads", "tails"])
print(coin)
"""

## using only the choice portion of the Random module
"""
from random import choice

coin = choice(["Heads", "Tails"])
print(coin)
"""

## Using "randint" with the Random module to print a random number between 1 and 10
"""
import random

number = random.randint(1, 10)
print(number)
"""

## using random module to create a card shuffle
"""
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
"""

## Using the Statistics module

import statistics

print(statistics.mean([100, 90]))