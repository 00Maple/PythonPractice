### Creating lists

"""
students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
"""

## Using a loop to iterate over the list
"""
students = ["Hermoine", "Harry", "Ron"]

for student in students:
    print(student)
"""

## Length check in a list
"""
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
"""

## Creating dictionaries(dict) for a list 

# Using list to create a dictionary
"""
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
"""
# this method is cumbersome for when lists grow larger

## Improved code using a dict
"""
students = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""

## Improved dict code

"""
students = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

for student in students:
    print(student, students[student], sep = ", ") 
"""
# add ', students[student]' to print names and houses clean up adding ', sep=", " '

## Additional data dict

students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")