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
"""
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()
"""

## Modifying above code packing the tuple into a variable
"""
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
"""

## Same as above but indexing into a tuple "programming defensively"
"""
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
"""

## Improving the code with a list to allow for flexibility
"""
def main():
    student = get_student()
    if student[0] == "Padme":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
# lists are mutable, order of house and name can be switched by a programmer, can be utilized in some cases to allow for further flexibility at the cost of code security.
if __name__ == "__main__":
    main()
"""

## Further improving above code - adding a dictionary
# two key-value pairs are returned in this case, advantage of this approach is we can index into this dictionary using keys
"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
"""

## More improvements to above code - removing unnecessary variable "student = {}" creates empty dict
"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
"""

## utilize braces "{}" in the return statement to create dictionary and condense to one line and return 
## at the same time
## Providing special case for padma in this dict
"""
def main():
    student = get_student()
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
"""

### CLASSES

## implementing our own class "student" to create our own data and name it
## A class is like a mold for a type of data where we can invent our own data type and give them a name
## Classes create a blueprint to create something, that something is an "object" or an "instance"
## in this case "student" is an object.
## utilizing the "..." notation accesses the attributes of the variable "student" of class student
"""
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
"""

## improvement of code above, laying some groundwork for the attributes expected inside an object whose
## class is "Student"
"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
"""

## Simplifying above code
"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
## line 203 simplifies lines 181-182
    return Student(name, house)

if __name__ == "__main__":
    main()
"""

## using Raise to prevent user error/provide explanation on what the error is
"""
class Student:
    def __init__(self, name, house):
        # Checks if name value entered throws an error if input is empty
        if not name:
            raise ValueError("Missing name")
        # Checks for proper house value entered throws an error if incorrect
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
"""

## Create a specific function where you can print attributes of an object.
"""
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

def __str__(self):
    return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
"""

## __str__ from above, is a built-in method that comes with Python classes provides a means by which a
## student is returned when called, so you can now as the programmer print an object, its attributes
## or anything you want related to the object

class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

def __str__(self):
    return f"{self.name} from {self.house}"

def charm(self):
    match self.patronus:
        case "Stag":
            return "🐴"
        case "Otter":
            return "🦦"
        case "Jack Russell terrier":
            return "🐕"
        case _:
            return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()


