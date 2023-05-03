## Using PyTest to test hello.py
""" Unnecessary code
def main():
    name = input("What is your name?")
    hello(name)

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
"""
"""
from hello import hello

def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"
"""

from hello import hello

def test_hello():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"