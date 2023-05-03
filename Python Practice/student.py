### OBJECT ORIENTED PROGRAMMING

## Step by step paradigm
"""
name =input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
"""

## Functions to abstract away parts of the SBS Paradigm
"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()
    """
## further modified code to store the student as a "tuple" tuples cannot be modified, in spirit we are returning two values

def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()